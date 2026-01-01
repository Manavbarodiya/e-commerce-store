from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from decimal import Decimal
import json

from .models import Product, Order, OrderItem
from .forms import UserRegistrationForm, LoginForm, CheckoutForm, SearchForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def offers(request):
    return render(request, 'offers.html')


def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products': products})


def search(request):
    form = SearchForm(request.GET)
    products = Product.objects.none()
    query = ''

    if form.is_valid():
        query = form.cleaned_data.get('query', '').strip()
        if query:
            products = Product.objects.filter(Q(name__icontains=query))
        else:
            products = Product.objects.all()

    context = {
        'products': products,
        'query': query,
        'count': products.count(),
        'form': form,
    }
    return render(request, 'cart.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})


def signout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        cart_data = request.POST.get('cart_data')

        if not cart_data:
            form.add_error(None, 'Cart is empty. Please add items to cart before checkout.')
            return render(request, 'checkout.html', {'form': form})

        try:
            cart = json.loads(cart_data)
            if not cart or len(cart) == 0:
                form.add_error(None, 'Cart is empty. Please add items to cart before checkout.')
                return render(request, 'checkout.html', {'form': form})

            if form.is_valid():
                shipping_address = form.cleaned_data['shipping_address']
                contact_number = form.cleaned_data['contact_number']

                with transaction.atomic():
                    total_amount = Decimal('0.00')
                    order_items_data = []

                    for product_id, item in cart.items():
                        try:
                            product = Product.objects.get(id=product_id)
                            quantity = int(item.get('quantity', 0))
                            price = Decimal(str(item.get('price', 0)))

                            if quantity > 0 and price > 0:
                                subtotal = price * quantity
                                total_amount += subtotal
                                order_items_data.append({
                                    'product': product,
                                    'quantity': quantity,
                                    'price': price,
                                    'subtotal': subtotal
                                })
                        except (Product.DoesNotExist, ValueError, TypeError):
                            continue

                    if total_amount <= 0 or not order_items_data:
                        form.add_error(None, 'Invalid order. Please check your cart items.')
                        return render(request, 'checkout.html', {'form': form})

                    order = Order.objects.create(
                        user=request.user,
                        total_amount=total_amount,
                        shipping_address=shipping_address,
                        contact_number=contact_number,
                        status='confirmed'
                    )

                    for item_data in order_items_data:
                        OrderItem.objects.create(
                            order=order,
                            product=item_data['product'],
                            quantity=item_data['quantity'],
                            price=item_data['price'],
                            subtotal=item_data['subtotal']
                        )

                    return redirect('order_confirmation', order_id=order.id)

        except json.JSONDecodeError:
            form.add_error(None, 'Invalid cart data. Please try again.')
        except Exception as e:
            form.add_error(None, 'An error occurred while processing your order. Please try again.')

        return render(request, 'checkout.html', {'form': form})

    form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})


@login_required(login_url='login')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})


@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})
