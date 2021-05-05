#!/bin/sh
# Run using sudo

apt update
apt install -y python-setuptools python-pip
apt install -y redis-server
apt install -y apache2 libapache2-mod-wsgi
apt install -y nodejs
apt install -y npm

cd /var/www
chmod +x init.sh
./init.sh

# Setup apache
cat > /etc/apache2/sites-available/BhavCopyWebsite.conf <<EOF
<VirtualHost *:80>
ServerName zerodha-machine # use the actual name of the machine being used
</VirtualHost>

Alias /static/ /var/www/BhavCopyWebsite/BhavCopyWebsite/static/

<Directory /var/www/BhavCopyWebsite/BhavCopyWebsite/static>
Require all granted
</Directory>

WSGIScriptAlias / /var/www/BhavCopyWebsite/BhavCopyWebsite/wsgi.py

<Directory /var/www/BhavCopyWebsite/BhavCopyWebsite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

WSGIPythonPath /var/www/BhavCopyWebsite
EOF

a2ensite BhavCopyWebsite
service apache2 reload
