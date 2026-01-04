from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('hygiene', 'Hygiene & Personal Care'),
        ('snacks', 'Snacks'),
        ('electronics', 'Electronic Products'),
        ('drawing', 'Drawing & Painting'),
        ('frozen', 'Frozen Food'),
        ('wellness', 'Sexual Wellness Products'),
        ('medical', 'Medical Products'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=50, help_text="e.g. kg, litre, packet")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='groceries')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - ₹{self.total_amount}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price at time of order
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} - Order #{self.order.id}"
    
    def save(self, *args, **kwargs):
        self.subtotal = Decimal(str(self.price)) * Decimal(str(self.quantity))
        super().save(*args, **kwargs)
