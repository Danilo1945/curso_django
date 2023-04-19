from django.db import models


# Create your models here.
class Product(models.Model):
    product_type_choices = (
        ('service', 'Servicio'),
        ('product', 'Almacenable'),
        ('consu', 'Consumible'),
    )

    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=20, choices=product_type_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name