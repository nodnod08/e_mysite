from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=19, decimal_places=3)
    product_type = models.CharField(max_length=100)

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
