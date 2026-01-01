# Quick Basket

A full-featured e-commerce web application built with Django.

## 🚀 Features

- **User Authentication**: Secure signup, login, and logout functionality
- **Product Catalog**: Browse products by category with search functionality
- **Shopping Cart**: Add and manage items in cart
- **Order Management**: Place orders and view order history
- **Admin Panel**: Manage products and orders through Django admin

## 🛠️ Tech Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render (with Gunicorn & WhiteNoise)

## 📋 Prerequisites

- Python 3.11+
- pip

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Manavbarodiya/e-commerce-store.git
   cd e-commerce-store
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Setup initial data:
   ```bash
   python manage.py setup_data
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

7. Open browser: http://127.0.0.1:8000/

## 📁 Project Structure

```
store/
├── myapp/              # Main application
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── forms.py       # Django forms
│   └── admin.py       # Admin configuration
├── templates/          # HTML templates
├── static/             # CSS, JS, Images
└── store/              # Project settings
```

## 🎯 Usage

1. **Sign Up**: Create a new account
2. **Browse**: Explore products by category or search
3. **Add to Cart**: Select items and add to shopping cart
4. **Checkout**: Enter shipping details and place order
5. **View Orders**: Check order history in "My Orders"

## 🌐 Live Demo

Visit: https://e-commerce-store-2bqi.onrender.com

## 👤 Contact

- **Email**: 2002manavbarodiya@gmail.com
- **Phone**: +91 9691829003

## 📝 License

This project is open source and available for educational purposes.

