from django.urls import path
from django.contrib import admin
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('offers/', views.offers, name='offers'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('', views.signin, name='login'),
    path("checkout/", views.checkout, name="checkout"),
    path("order/confirmation/<int:order_id>/", views.order_confirmation, name="order_confirmation"),
    path("orders/", views.order_history, name="order_history"),
]
