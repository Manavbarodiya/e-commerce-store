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
            {'name': 'Rice', 'price': 50.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Wheat Flour', 'price': 40.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Sugar', 'price': 45.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Salt', 'price': 20.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Cooking Oil', 'price': 120.00, 'unit': 'litre', 'category': 'groceries'},
            {'name': 'Milk', 'price': 60.00, 'unit': 'litre', 'category': 'groceries'},
            {'name': 'Bread', 'price': 30.00, 'unit': 'packet', 'category': 'groceries'},
            {'name': 'Eggs', 'price': 80.00, 'unit': 'dozen', 'category': 'groceries'},
            {'name': 'Onions', 'price': 30.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Tomatoes', 'price': 40.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Potatoes', 'price': 25.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Bananas', 'price': 50.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Apples', 'price': 120.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Lentils (Dal)', 'price': 80.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Chickpeas', 'price': 90.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Black Gram', 'price': 85.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Turmeric Powder', 'price': 150.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Red Chili Powder', 'price': 200.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Cumin Seeds', 'price': 300.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Coriander Seeds', 'price': 250.00, 'unit': 'kg', 'category': 'groceries'},
            
            # Hygiene & Personal Care
            {'name': 'Soap', 'price': 40.00, 'unit': 'packet', 'category': 'hygiene'},
            {'name': 'Shampoo', 'price': 150.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Toothpaste', 'price': 80.00, 'unit': 'tube', 'category': 'hygiene'},
            {'name': 'Toothbrush', 'price': 50.00, 'unit': 'piece', 'category': 'hygiene'},
            {'name': 'Face Wash', 'price': 120.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Body Lotion', 'price': 200.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Deodorant', 'price': 180.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Hair Oil', 'price': 250.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Conditioner', 'price': 160.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Hand Sanitizer', 'price': 100.00, 'unit': 'bottle', 'category': 'hygiene'},
            {'name': 'Tissue Paper', 'price': 60.00, 'unit': 'packet', 'category': 'hygiene'},
            {'name': 'Wet Wipes', 'price': 80.00, 'unit': 'packet', 'category': 'hygiene'},
            
            # Snacks
            {'name': 'Biscuits', 'price': 30.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Chocolate', 'price': 50.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Potato Chips', 'price': 40.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Namkeen', 'price': 60.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Cookies', 'price': 45.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Candy', 'price': 25.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Nuts Mix', 'price': 200.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Popcorn', 'price': 35.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Energy Bar', 'price': 50.00, 'unit': 'packet', 'category': 'snacks'},
            {'name': 'Dry Fruits', 'price': 500.00, 'unit': 'kg', 'category': 'snacks'},
            
            # Electronic Products
            {'name': 'LED Television', 'price': 25000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Refrigerator', 'price': 30000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Air Fryer', 'price': 8000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Microwave Oven', 'price': 12000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Washing Machine', 'price': 20000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Electric Kettle', 'price': 1500.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Mixer Grinder', 'price': 3000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Iron', 'price': 2000.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Hair Dryer', 'price': 1500.00, 'unit': 'piece', 'category': 'electronics'},
            {'name': 'Electric Heater', 'price': 2500.00, 'unit': 'piece', 'category': 'electronics'},
            
            # Drawing & Painting
            {'name': 'Paint Brushes Set', 'price': 300.00, 'unit': 'set', 'category': 'drawing'},
            {'name': 'Water Colors', 'price': 250.00, 'unit': 'set', 'category': 'drawing'},
            {'name': 'Oil Paints', 'price': 500.00, 'unit': 'set', 'category': 'drawing'},
            {'name': 'Sketchbook', 'price': 150.00, 'unit': 'piece', 'category': 'drawing'},
            {'name': 'Drawing Pencils Set', 'price': 200.00, 'unit': 'set', 'category': 'drawing'},
            {'name': 'Canvas', 'price': 400.00, 'unit': 'piece', 'category': 'drawing'},
            {'name': 'Eraser', 'price': 20.00, 'unit': 'piece', 'category': 'drawing'},
            {'name': 'Sharpener', 'price': 15.00, 'unit': 'piece', 'category': 'drawing'},
            {'name': 'Color Pencils', 'price': 180.00, 'unit': 'set', 'category': 'drawing'},
            {'name': 'Marker Pens Set', 'price': 220.00, 'unit': 'set', 'category': 'drawing'},
            
            # Frozen Food
            {'name': 'Frozen Vegetables', 'price': 80.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen Peas', 'price': 70.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen Corn', 'price': 60.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Ice Cream', 'price': 150.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen Paratha', 'price': 100.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen Samosa', 'price': 120.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen Chicken', 'price': 300.00, 'unit': 'kg', 'category': 'frozen'},
            {'name': 'Frozen Fish', 'price': 250.00, 'unit': 'kg', 'category': 'frozen'},
            {'name': 'Frozen Pizza', 'price': 200.00, 'unit': 'packet', 'category': 'frozen'},
            {'name': 'Frozen French Fries', 'price': 90.00, 'unit': 'packet', 'category': 'frozen'},
            
            # Sexual Wellness Products
            {'name': 'Condoms', 'price': 150.00, 'unit': 'packet', 'category': 'wellness'},
            {'name': 'Lubricant', 'price': 300.00, 'unit': 'bottle', 'category': 'wellness'},
            {'name': 'Massage Oil', 'price': 250.00, 'unit': 'bottle', 'category': 'wellness'},
            {'name': 'Wellness Tablets', 'price': 500.00, 'unit': 'packet', 'category': 'wellness'},
            {'name': 'Intimate Wash', 'price': 200.00, 'unit': 'bottle', 'category': 'wellness'},
            
            # Medical Products
            {'name': 'Paracetamol Tablets', 'price': 50.00, 'unit': 'strip', 'category': 'medical'},
            {'name': 'Antibiotic Capsules', 'price': 150.00, 'unit': 'strip', 'category': 'medical'},
            {'name': 'Cough Syrup', 'price': 120.00, 'unit': 'bottle', 'category': 'medical'},
            {'name': 'Bandage', 'price': 40.00, 'unit': 'packet', 'category': 'medical'},
            {'name': 'Antiseptic Solution', 'price': 80.00, 'unit': 'bottle', 'category': 'medical'},
            {'name': 'Gauze Pads', 'price': 60.00, 'unit': 'packet', 'category': 'medical'},
            {'name': 'Thermometer', 'price': 200.00, 'unit': 'piece', 'category': 'medical'},
            {'name': 'Blood Pressure Monitor', 'price': 1500.00, 'unit': 'piece', 'category': 'medical'},
            {'name': 'First Aid Kit', 'price': 300.00, 'unit': 'kit', 'category': 'medical'},
            {'name': 'Vitamin Tablets', 'price': 250.00, 'unit': 'bottle', 'category': 'medical'},
            
            # Additional items
            {'name': 'Tea', 'price': 200.00, 'unit': 'kg', 'category': 'groceries'},
            {'name': 'Coffee', 'price': 300.00, 'unit': 'kg', 'category': 'groceries'},
        ]

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'price': product_data['price'], 
                    'unit': product_data['unit'],
                    'category': product_data.get('category', 'groceries')
                }
            )
            # Update category if product already exists but category is missing
            if not created and not product.category:
                product.category = product_data.get('category', 'groceries')
                product.save()
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Created {created_count} products'))

