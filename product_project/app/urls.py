from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('product_view', views.product_view, name='product_view'),
    path('category', views.category, name='category'),
    path('sales', views.sales, name='sales'),
    path('customer', views.customer, name='customer'),
]