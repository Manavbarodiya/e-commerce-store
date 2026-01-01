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
    
    # Setup initial data (superuser and products)
    print("Setting up initial data...")
    try:
        call_command('setup_data', verbosity=2)
        print("✓ Initial data setup completed")
        
        # Verify admin user was created/updated
        from django.contrib.auth.models import User
        admin = User.objects.filter(username='admin').first()
        if admin:
            print(f"✓ Admin user verified: username='{admin.username}', is_staff={admin.is_staff}, is_superuser={admin.is_superuser}")
        else:
            print("✗ WARNING: Admin user not found after setup!")
    except Exception as e:
        import traceback
        print(f"⚠ WARNING: Initial data setup failed: {e}")
        print(traceback.format_exc())
        # Continue anyway - don't exit
    
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

