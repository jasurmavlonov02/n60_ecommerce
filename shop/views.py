from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView

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


class Index(View):
    def get(self, request, category_id=None):
        categories = Category.objects.all()
        products = Product.objects.all()
        if category_id:
            products = Product.objects.filter(category=category_id)
            context = {'products': products}
            return render(request, 'shop/product-list.html', context)
        context = {'categories': categories, 'products': products}
        return render(request, 'shop/index.html', context)


# class ProductDetail(TemplateView):
#     template_name = 'shop/product-detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetail, self).get_context_data(**kwargs)
#         context['product'] = Product.objects.get(id=self.kwargs['product_id'])
#         return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
