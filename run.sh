#!/bin/bash
echo "Setting up Audio Cleaner virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting Application..."
python app.py
