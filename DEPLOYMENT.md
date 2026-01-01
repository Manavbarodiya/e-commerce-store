# Deployment Guide for Django E-Commerce Store

## Why Netlify Won't Work
Netlify is for **static sites only** (HTML, CSS, JavaScript). Django is a **Python web framework** that needs a server to run, so it cannot be hosted on Netlify.

## Recommended Platform: Render (Free)

### Step 1: Create Account
1. Go to https://render.com
2. Sign up with GitHub (connect your GitHub account)

### Step 2: Deploy on Render
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `Manavbarodiya/e-commerce-store`
3. Configure:
   - **Name**: ecommerce-store (or any name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn store.wsgi:application`
4. Click "Create Web Service"

### Step 3: Configure Environment Variables
In Render dashboard, go to Environment tab and add:
- `SECRET_KEY`: Generate a new secret key (you can use: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: Your Render URL (e.g., `ecommerce-store.onrender.com`)

### Step 4: Update settings.py (Already Done)
The settings.py has been updated with:
- WhiteNoise for static files
- STATIC_ROOT for production

### Step 5: Deploy
1. Render will automatically build and deploy
2. Wait for deployment to complete
3. Your site will be available at: `https://your-app-name.onrender.com`

## Alternative Platforms

### Railway (Free Tier)
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Django and deploys

### PythonAnywhere (Free Tier)
1. Go to https://www.pythonanywhere.com
2. Create free account
3. Go to Web tab → "Add a new web app"
4. Follow their Django deployment guide

### Heroku (Paid - $5/month minimum)
1. Go to https://heroku.com
2. Create account
3. Install Heroku CLI
4. Deploy using Git

## Notes
- The free tier on Render has a **cold start** (15-30 seconds on first load after inactivity)
- Database: For production, consider PostgreSQL (Render provides free PostgreSQL)
- Static files: Configured with WhiteNoise (already added)

