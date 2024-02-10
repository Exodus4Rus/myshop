from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'index.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
