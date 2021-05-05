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
2. Download redis, if required: `sudo apt update && sudo apt install -y redis-server` (For more info, check [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04))
3. The `BhavCopyWebsite` folder contains an `example.env` file. Create a `.env` file in the same folder, with the proper values, using the example file as reference.
4. Run the `setup.sh` file located in the repository root: `bash -x setup.sh`
5. Run the python server

## Deploying to production
1. `cd /var/www`
2. `git clone https://github.com/AliabbasMerchant/BhavCopyWebsite`
4. `sudo chmod +x deploy.sh`
3. `sudo ./deploy.sh`

## Live Demo
A live version of the website is hosted at: [52.230.0.192](http://52.230.0.192)
(Microsoft Azure VM)
