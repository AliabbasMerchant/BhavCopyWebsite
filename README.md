# BhavCopyWebsite
Website to Show the latest BhavCopy Data 

## Description
This is a standalone Python Django web app/server that:
- Downloads the equity bhavcopy zip from the BhavCopy page (https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx) every day at 18:00 IST for the current date.
- Extracts and parses the CSV file in it.
- Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally downloads the results as CSV.
- Performs the search on the backend using Redis.

## Tech Stack
Django, Vue

## Requirements
1. Redis access (local/remote) -> Details to be configured in the `.env` file

## Setup Instructions
1. Download the source code
2. Install redis, if l: `sudo apt update && sudo apt install -y redis-server` (For more info, check [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04))
3. The `BhavCopyWebsite/BhavCopyWebsite` folder contains an `example.env` file. Create a `.env` file in the same folder, with the proper values, using the example file as reference.
4. Run the `init.sh` file located in the repository root: `bash -x init.sh`
5. `cd BhavCopyWebsite`
6. Run the Django migrations: `python3 manage.py migrate`
7. Start the server: `python3 manage.py runserver`

## Deploying to production [tested on a Linux (ubuntu 18.04) VM]
1. `cd /var/www`
2. `sudo git clone https://github.com/AliabbasMerchant/BhavCopyWebsite`
3. `cd BhavCopyWebsite`
4. Create a `.env` file in `BhavCopyWebsite\BhavCopyWebsite`, using `example.env` as reference
4. `sudo chmod +x deploy.sh`
5. `bash -x ./deploy.sh`

## Live Demo
A live version of the website is hosted at: [52.230.0.192](http://52.230.0.192)
(Microsoft Azure VM)
