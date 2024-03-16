from django.shortcuts import render
from .models import Product


def shop(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})
