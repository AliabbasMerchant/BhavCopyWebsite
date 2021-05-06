#!/bin/bash

# Create the required folders
mkdir -p BhavCopyWebsite/data
mkdir -p BhavCopyWebsite/logs

# Setup the python environment
python3 -m pip install -r requirements.txt

# Setup the node environment
cd BhavCopyWebsite/frontend
npm install

# Build the frontend
npm run build

# Come back to the original repo root folder
cd ../..
