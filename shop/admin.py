from django.contrib import admin

from shop.models import Category, Product, Images, Attribute, AttributeValue, ProductAttribute

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)

admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
