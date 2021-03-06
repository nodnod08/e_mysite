# Generated by Django 3.2.5 on 2021-07-27 14:31

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_products_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_photo',
            field=models.ImageField(max_length=300, null=True, upload_to=product.models.Products.product_directory_path),
        ),
    ]
