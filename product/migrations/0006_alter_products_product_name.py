# Generated by Django 3.2 on 2021-07-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_products_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]