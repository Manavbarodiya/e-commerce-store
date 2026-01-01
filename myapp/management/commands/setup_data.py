from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Product


class Command(BaseCommand):
    help = 'Creates superuser and initial products'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@quickbasket.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin'))
        else:
            self.stdout.write('Superuser already exists')

        # Create sample products if they don't exist
        products_data = [
            {'name': 'Rice', 'price': 50.00, 'unit': 'kg'},
            {'name': 'Wheat Flour', 'price': 40.00, 'unit': 'kg'},
            {'name': 'Sugar', 'price': 45.00, 'unit': 'kg'},
            {'name': 'Salt', 'price': 20.00, 'unit': 'kg'},
            {'name': 'Cooking Oil', 'price': 120.00, 'unit': 'litre'},
            {'name': 'Milk', 'price': 60.00, 'unit': 'litre'},
            {'name': 'Bread', 'price': 30.00, 'unit': 'packet'},
            {'name': 'Eggs', 'price': 80.00, 'unit': 'dozen'},
            {'name': 'Onions', 'price': 30.00, 'unit': 'kg'},
            {'name': 'Tomatoes', 'price': 40.00, 'unit': 'kg'},
            {'name': 'Potatoes', 'price': 25.00, 'unit': 'kg'},
            {'name': 'Bananas', 'price': 50.00, 'unit': 'kg'},
            {'name': 'Apples', 'price': 120.00, 'unit': 'kg'},
            {'name': 'Soap', 'price': 40.00, 'unit': 'packet'},
            {'name': 'Shampoo', 'price': 150.00, 'unit': 'bottle'},
            {'name': 'Toothpaste', 'price': 80.00, 'unit': 'tube'},
            {'name': 'Biscuits', 'price': 30.00, 'unit': 'packet'},
            {'name': 'Chocolate', 'price': 50.00, 'unit': 'packet'},
            {'name': 'Tea', 'price': 200.00, 'unit': 'kg'},
            {'name': 'Coffee', 'price': 300.00, 'unit': 'kg'},
        ]

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={'price': product_data['price'], 'unit': product_data['unit']}
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Created {created_count} products'))

