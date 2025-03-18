from django.contrib import admin

from shop.models import Category, Product, Images

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
