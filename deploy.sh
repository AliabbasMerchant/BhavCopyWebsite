#!/bin/sh

sudo unlink /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

sudo apt update
sudo apt install -y python3-setuptools python3-pip
sudo apt install -y redis-server
sudo apt install -y apache2 libapache2-mod-wsgi-py3
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install 14.15.4

sudo chown -R $(whoami) ~/.nvm
sudo chown -R $(whoami) /var/www/BhavCopyWebsite/
sudo chmod -R 777 /var/www/BhavCopyWebsite/

sudo chmod +x init.sh
./init.sh

cd BhavCopyWebsite
python3 manage.py collectstatic
python3 manage.py migrate

# Setup apache
sudo chown -R $(whoami) /etc/apache2/sites-available/
cat > /etc/apache2/sites-available/BhavCopyWebsite.conf <<EOF
<VirtualHost *:80>
#Use the actual name of the machine being used
ServerName zerodha-machine
</VirtualHost>

Alias /static/ /var/www/BhavCopyWebsite/BhavCopyWebsite/static/

<Directory /var/www/BhavCopyWebsite/BhavCopyWebsite/static>
Require all granted
</Directory>

WSGIScriptAlias / /var/www/BhavCopyWebsite/BhavCopyWebsite/BhavCopyWebsite/wsgi.py

<Directory /var/www/BhavCopyWebsite/BhavCopyWebsite/BhavCopyWebsite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

WSGIPythonPath /var/www/BhavCopyWebsite/BhavCopyWebsite
EOF

sudo a2ensite BhavCopyWebsite
sudo systemctl reload apache2
