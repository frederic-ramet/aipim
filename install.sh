#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting installation process..."

echo "Installing frontend"
cd frontend
echo "Current directory: $(pwd)"
pip install -r requirements.txt
echo "Frontend dependencies installed successfully."

echo "Installing backend"
cd ../backend
echo "Current directory: $(pwd)"
pip install -r requirements.txt
echo "Backend dependencies installed successfully."

DB_PATH="./ai-pim.db"  # adjust the path as needed
if [ -f "$DB_PATH" ]; then
    echo "Removing existing database file at $DB_PATH."
    rm "$DB_PATH"
    echo "Database file removed."
else
    echo "No existing database file found at $DB_PATH."
fi

echo "Setting up database..."
python create_database.py
echo "Database setup completed."

cd ../
echo "Current directory: $(pwd)"
echo "Installation Done"
