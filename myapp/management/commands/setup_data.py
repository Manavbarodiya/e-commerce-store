from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Product


class Command(BaseCommand):
    help = 'Creates superuser and initial products'

    def handle(self, *args, **options):
        # Create or update superuser
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@quickbasket.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        
        # Always set the password to 'admin' (in case user already existed)
        admin_user.set_password('admin')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.email = 'admin@quickbasket.com'
        admin_user.save()
        
        if created:
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser password updated: admin/admin'))

        # Create sample products covering all homepage categories
        products_data = [
            # Groceries
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
            {'name': 'Lentils (Dal)', 'price': 80.00, 'unit': 'kg'},
            {'name': 'Chickpeas', 'price': 90.00, 'unit': 'kg'},
            {'name': 'Black Gram', 'price': 85.00, 'unit': 'kg'},
            {'name': 'Turmeric Powder', 'price': 150.00, 'unit': 'kg'},
            {'name': 'Red Chili Powder', 'price': 200.00, 'unit': 'kg'},
            {'name': 'Cumin Seeds', 'price': 300.00, 'unit': 'kg'},
            {'name': 'Coriander Seeds', 'price': 250.00, 'unit': 'kg'},
            
            # Hygiene & Personal Care
            {'name': 'Soap', 'price': 40.00, 'unit': 'packet'},
            {'name': 'Shampoo', 'price': 150.00, 'unit': 'bottle'},
            {'name': 'Toothpaste', 'price': 80.00, 'unit': 'tube'},
            {'name': 'Toothbrush', 'price': 50.00, 'unit': 'piece'},
            {'name': 'Face Wash', 'price': 120.00, 'unit': 'bottle'},
            {'name': 'Body Lotion', 'price': 200.00, 'unit': 'bottle'},
            {'name': 'Deodorant', 'price': 180.00, 'unit': 'bottle'},
            {'name': 'Hair Oil', 'price': 250.00, 'unit': 'bottle'},
            {'name': 'Conditioner', 'price': 160.00, 'unit': 'bottle'},
            {'name': 'Hand Sanitizer', 'price': 100.00, 'unit': 'bottle'},
            {'name': 'Tissue Paper', 'price': 60.00, 'unit': 'packet'},
            {'name': 'Wet Wipes', 'price': 80.00, 'unit': 'packet'},
            
            # Snacks
            {'name': 'Biscuits', 'price': 30.00, 'unit': 'packet'},
            {'name': 'Chocolate', 'price': 50.00, 'unit': 'packet'},
            {'name': 'Potato Chips', 'price': 40.00, 'unit': 'packet'},
            {'name': 'Namkeen', 'price': 60.00, 'unit': 'packet'},
            {'name': 'Cookies', 'price': 45.00, 'unit': 'packet'},
            {'name': 'Candy', 'price': 25.00, 'unit': 'packet'},
            {'name': 'Nuts Mix', 'price': 200.00, 'unit': 'packet'},
            {'name': 'Popcorn', 'price': 35.00, 'unit': 'packet'},
            {'name': 'Energy Bar', 'price': 50.00, 'unit': 'packet'},
            {'name': 'Dry Fruits', 'price': 500.00, 'unit': 'kg'},
            
            # Electronic Products
            {'name': 'LED Television', 'price': 25000.00, 'unit': 'piece'},
            {'name': 'Refrigerator', 'price': 30000.00, 'unit': 'piece'},
            {'name': 'Air Fryer', 'price': 8000.00, 'unit': 'piece'},
            {'name': 'Microwave Oven', 'price': 12000.00, 'unit': 'piece'},
            {'name': 'Washing Machine', 'price': 20000.00, 'unit': 'piece'},
            {'name': 'Electric Kettle', 'price': 1500.00, 'unit': 'piece'},
            {'name': 'Mixer Grinder', 'price': 3000.00, 'unit': 'piece'},
            {'name': 'Iron', 'price': 2000.00, 'unit': 'piece'},
            {'name': 'Hair Dryer', 'price': 1500.00, 'unit': 'piece'},
            {'name': 'Electric Heater', 'price': 2500.00, 'unit': 'piece'},
            
            # Drawing & Painting
            {'name': 'Paint Brushes Set', 'price': 300.00, 'unit': 'set'},
            {'name': 'Water Colors', 'price': 250.00, 'unit': 'set'},
            {'name': 'Oil Paints', 'price': 500.00, 'unit': 'set'},
            {'name': 'Sketchbook', 'price': 150.00, 'unit': 'piece'},
            {'name': 'Drawing Pencils Set', 'price': 200.00, 'unit': 'set'},
            {'name': 'Canvas', 'price': 400.00, 'unit': 'piece'},
            {'name': 'Eraser', 'price': 20.00, 'unit': 'piece'},
            {'name': 'Sharpener', 'price': 15.00, 'unit': 'piece'},
            {'name': 'Color Pencils', 'price': 180.00, 'unit': 'set'},
            {'name': 'Marker Pens Set', 'price': 220.00, 'unit': 'set'},
            
            # Frozen Food
            {'name': 'Frozen Vegetables', 'price': 80.00, 'unit': 'packet'},
            {'name': 'Frozen Peas', 'price': 70.00, 'unit': 'packet'},
            {'name': 'Frozen Corn', 'price': 60.00, 'unit': 'packet'},
            {'name': 'Ice Cream', 'price': 150.00, 'unit': 'packet'},
            {'name': 'Frozen Paratha', 'price': 100.00, 'unit': 'packet'},
            {'name': 'Frozen Samosa', 'price': 120.00, 'unit': 'packet'},
            {'name': 'Frozen Chicken', 'price': 300.00, 'unit': 'kg'},
            {'name': 'Frozen Fish', 'price': 250.00, 'unit': 'kg'},
            {'name': 'Frozen Pizza', 'price': 200.00, 'unit': 'packet'},
            {'name': 'Frozen French Fries', 'price': 90.00, 'unit': 'packet'},
            
            # Sexual Wellness Products
            {'name': 'Condoms', 'price': 150.00, 'unit': 'packet'},
            {'name': 'Lubricant', 'price': 300.00, 'unit': 'bottle'},
            {'name': 'Massage Oil', 'price': 250.00, 'unit': 'bottle'},
            {'name': 'Wellness Tablets', 'price': 500.00, 'unit': 'packet'},
            {'name': 'Intimate Wash', 'price': 200.00, 'unit': 'bottle'},
            
            # Medical Products
            {'name': 'Paracetamol Tablets', 'price': 50.00, 'unit': 'strip'},
            {'name': 'Antibiotic Capsules', 'price': 150.00, 'unit': 'strip'},
            {'name': 'Cough Syrup', 'price': 120.00, 'unit': 'bottle'},
            {'name': 'Bandage', 'price': 40.00, 'unit': 'packet'},
            {'name': 'Antiseptic Solution', 'price': 80.00, 'unit': 'bottle'},
            {'name': 'Gauze Pads', 'price': 60.00, 'unit': 'packet'},
            {'name': 'Thermometer', 'price': 200.00, 'unit': 'piece'},
            {'name': 'Blood Pressure Monitor', 'price': 1500.00, 'unit': 'piece'},
            {'name': 'First Aid Kit', 'price': 300.00, 'unit': 'kit'},
            {'name': 'Vitamin Tablets', 'price': 250.00, 'unit': 'bottle'},
            
            # Additional items
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

