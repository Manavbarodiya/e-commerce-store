#!/usr/bin/env bash
# Run migrations on startup (important for SQLite on Render)
python manage.py migrate --noinput
# Start the application
gunicorn store.wsgi:application

