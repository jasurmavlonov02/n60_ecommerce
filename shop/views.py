from django.shortcuts import render

from shop.models import Category, Product


# Create your views here.


def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
        context = {'products': products}
        return render(request, 'shop/product-list.html', context)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'shop/product-detail.html', context)
