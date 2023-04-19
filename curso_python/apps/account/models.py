from django.db import models

# Create your models here.
from django.db import models

from apps.product.models import Product
from apps.res.models import Partner


# Create your models here.
class Move(models.Model):
    name = models.CharField(max_length=50)
    cliente = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date = models.DateField()
    numero_documento = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class MoveLine(models.Model):
    move_factura = models.ForeignKey(Move, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.move_factura.name