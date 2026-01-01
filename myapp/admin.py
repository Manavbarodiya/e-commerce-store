from django.contrib import admin
from .models import Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'subtotal')
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount', 'status', 'contact_number')
    list_filter = ('status', 'order_date', 'created_at')
    search_fields = ('id', 'user__username', 'contact_number', 'shipping_address')
    readonly_fields = ('order_date', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    date_hierarchy = 'order_date'
    
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'order_date', 'status', 'total_amount')
        }),
        ('Shipping Information', {
            'fields': ('shipping_address', 'contact_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'subtotal')
    list_filter = ('order__status', 'order__order_date')
    search_fields = ('order__id', 'product__name')
    readonly_fields = ('subtotal',)    
