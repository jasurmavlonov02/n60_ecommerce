from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [

    path('', views.index, name='index'),
    path('products_list/<int:category_id>', views.index, name='products_list_by_category'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail')
]
