#!/usr/bin/env python
"""Startup script that ensures migrations run before starting the server."""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def main():
    print("=== Starting application ===")
    print(f"Current directory: {os.getcwd()}")
    print(f"Python version: {sys.version}")
    
    # Run migrations
    print("Running database migrations...")
    try:
        call_command('migrate', verbosity=1, interactive=False)
        print("✓ Migrations completed")
    except Exception as e:
        print(f"✗ ERROR: Migrations failed: {e}")
        sys.exit(1)
    
    # Verify database
    print("Verifying database setup...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'")
            result = cursor.fetchone()
            if result:
                print("✓ Database tables verified")
            else:
                print("✗ ERROR: auth_user table not found!")
                sys.exit(1)
    except Exception as e:
        print(f"✗ ERROR: Database verification failed: {e}")
        sys.exit(1)
    
    # Start gunicorn
    print("Starting gunicorn server...")
    os.execvp('gunicorn', ['gunicorn', 'store.wsgi:application'])

if __name__ == '__main__':
    main()

