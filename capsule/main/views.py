from django.shortcuts import render
from .models import *


def home(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    return render(request,
                  './index.html',
                  {
                      'products': products,
                      'banners': banners
                   }
                  )


def category(request):
    products = Product.objects.all()
    return render(request,
                  './category.html',
                  {
                      'products': products,
                   }
                  )


def search(request):
    if request.method == 'GET':
        searchbar = request.GET.get('searchbar')
        products = Product.objects.all().filter(name__icontains=searchbar)
        return render(request, './searchbar.html', {'products': products})