from decimal import Decimal

from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            discount_price = self.price * Decimal(1 - self.discount / 100)
            return Decimal(f'{discount_price}').quantize(Decimal('0.00'))

        return Decimal(f'{self.price}').quantize(Decimal('0.00'))

    @property
    def get_absolute_url(self):
        primary_image = self.images.all().order_by('my_order')[0]
        print(primary_image)
        return primary_image.image.url

    @property
    def attributes(self):
        return self.product_attributes.all()

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    my_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} {self.image.url}'

    class Meta:
        verbose_name_plural = "Images"


class Attribute(models.Model):
    attribute_key = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.attribute_key


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.attribute_value


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attributes')
    attribute_key_id = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    attribute_value_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} {self.attribute_key_id.attribute_key} {self.attribute_value_id.attribute_value}'
# x_object : ProductAttribute = product.product_attributes.all()
