#!/usr/bin/env bash
set -e  # Exit on error

echo "=== Starting application ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Run migrations on startup (critical for SQLite on Render's ephemeral filesystem)
echo "Running database migrations..."
python manage.py migrate --noinput

echo "Migrations completed successfully"

# Start the application
echo "Starting gunicorn server..."
exec gunicorn store.wsgi:application

