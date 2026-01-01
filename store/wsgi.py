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

# Fallback: Ensure migrations run on Render (ephemeral filesystem)
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
    except Exception as e:
        print(f"Error running migrations from WSGI: {e}")
        # Continue anyway - let requests handle errors
