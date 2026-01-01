"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

# Get the WSGI application
application = get_wsgi_application()

# Fallback: Ensure migrations and initial data setup on Render (ephemeral filesystem)
# This runs once when the WSGI application is loaded
if os.path.exists('/opt/render/project/src'):
    try:
        from django.db import connection
        from django.core.management import call_command
        
        # Check if auth_user table exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'")
            if not cursor.fetchone():
                print("Running migrations from WSGI (auth_user table not found)...")
                call_command('migrate', verbosity=1, interactive=False)
                print("Migrations completed from WSGI")
                
                # Setup initial data (admin user and products)
                print("Setting up initial data from WSGI...")
                call_command('setup_data', verbosity=1)
                print("Initial data setup completed from WSGI")
            else:
                # Table exists, but check if admin user exists
                from django.contrib.auth.models import User
                if not User.objects.filter(username='admin').exists():
                    print("Admin user not found, running setup_data from WSGI...")
                    call_command('setup_data', verbosity=1)
                    print("Initial data setup completed from WSGI")
    except Exception as e:
        import traceback
        print(f"Error in WSGI setup: {e}")
        print(traceback.format_exc())
        # Continue anyway - let requests handle errors
