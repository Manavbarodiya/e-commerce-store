#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Setting up initial data..."
python manage.py setup_data

echo "Collecting static files..."
python manage.py collectstatic --noinput



