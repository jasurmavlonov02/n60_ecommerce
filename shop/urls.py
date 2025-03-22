from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [

    path('', views.index, name='index'),
    path('products_list/<int:category_id>', views.Index.as_view(), name='products_list_by_category'),
    path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail')
]
