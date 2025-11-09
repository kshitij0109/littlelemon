from django.shortcuts import render, get_object_or_404
from .models import Menu

def index(request):
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def book(request):
    return render(request, 'restaurant/book.html')

def menu(request):
    items = Menu.objects.all().order_by('name')
    return render(request, 'restaurant/menu.html', {'items': items})

def menu_item(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, 'restaurant/menu_item.html', {'item': item})
