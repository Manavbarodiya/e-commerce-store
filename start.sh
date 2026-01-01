#!/usr/bin/env bash
set -e  # Exit on error

# Ensure database directory exists
mkdir -p "$(dirname db.sqlite3)" || true

# Run migrations on startup (important for SQLite on Render)
echo "Running database migrations..."
python manage.py migrate --noinput

# Start the application
echo "Starting gunicorn server..."
exec gunicorn store.wsgi:application

