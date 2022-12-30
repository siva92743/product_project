from django.shortcuts import render, redirect

from app.forms import Task, Item, Sell, User
from app.models import Equipments


def home(request):
    return render(request, 'home.html')


def product(request):
    data = Task()
    if request.method == 'POST':
        data = Task(request.POST)
        if data.is_valid():
            data.save()
            return redirect('product')
    return render(request, 'product.html', {'data': data})


def product_view(request):
    data = Equipments.objects.all()
    return render(request, 'product_view.html', {'data': data})


def category(request):
    data = Item()
    if request.method == 'POST':
        data = Item(request.POST)
        if data.is_valid():
            data.save()
            return redirect('category')
    return render(request, 'category.html', {'data': data})


def sales(request):
    data = Sell()
    if request.method == 'POST':
        data = Sell(request.POST)
        if data.is_valid():
            data.save()
            return redirect('sales')
    return render(request, 'sales.html', {'data': data})


def customer(request):
    data = User()
    if request.method == 'POST':
        data = User(request.POST)
        if data.is_valid():
            data.save()
            return redirect('customer')
    return render(request, 'customer.html', {'data': data})