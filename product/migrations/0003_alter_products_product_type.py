# Generated by Django 3.2.5 on 2021-07-18 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210718_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.producttype'),
        ),
    ]
