#!/usr/bin/env bash
set -e  # Exit on error

echo "=== Starting application ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Ensure we're in the right directory
cd /opt/render/project/src 2>/dev/null || true

# Run migrations on startup (critical for SQLite on Render's ephemeral filesystem)
echo "Running database migrations..."
python manage.py migrate --noinput

# Verify migrations by checking for auth_user table
echo "Verifying database setup..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'\")
result = cursor.fetchone()
if result:
    print('✓ Database tables verified')
else:
    print('✗ ERROR: Database tables not found!')
    exit(1)
" || {
    echo "ERROR: Database verification failed!"
    exit 1
}

echo "Migrations completed successfully"

# Start the application
echo "Starting gunicorn server..."
exec gunicorn store.wsgi:application

