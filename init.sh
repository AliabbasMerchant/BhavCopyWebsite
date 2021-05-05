#!/bin/bash

# Create the required folders
mkdir -p data
mkdir -p logs

# Setup the python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup the node environment
cd frontend
npm install

# Build the frontend
npm run build

cd ../..
