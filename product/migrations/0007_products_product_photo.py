# Generated by Django 3.2.5 on 2021-07-27 13:42

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_products_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_photo',
            field=models.ImageField(null=True, upload_to=product.models.Products.product_directory_path),
        ),
    ]