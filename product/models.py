from django.db import models
from datetime import datetime
from django.conf import settings
import uuid, os

class Products(models.Model):
    def product_directory_path(instance, filename):
        now = datetime.now()
        name = filename.split(".")[0]
        extension = filename.split(".")[1]
        file_name = name + "_" + now.strftime("%d-%m-%Y") + "_" + str(uuid.uuid4()) + "." + extension

        directory = 'product_files/product_photos'
        
        return '{0}/{1}'.format(directory, file_name)

    product_name = models.CharField(max_length=100, unique=False)
    product_price = models.DecimalField(max_digits=19, decimal_places=3)
    quantity = models.IntegerField(default=10)
    product_photo = models.ImageField(upload_to=product_directory_path, null=True, max_length=300)
    product_type = models.ForeignKey('ProductType', related_name='product_type', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_types'
