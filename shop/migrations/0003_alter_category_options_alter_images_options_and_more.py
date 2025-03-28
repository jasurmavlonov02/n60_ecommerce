# Generated by Django 5.1.7 on 2025-03-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='images',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
