from django.db import models

# Create your models here.
from django.db import models


class Canton(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()

    class Meta:
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantones'

    def __str__(self):
        return self.name


class Partner(models.Model):
    identification_choices = [
        ('cedula', 'Cédula'),
        ('ruc', 'RUC'),
        ('pasaporte', 'Pasaporte'),
    ]
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_type = models.CharField(max_length=20, choices=identification_choices)
    identification = models.CharField(max_length=13)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    canton = models.ForeignKey(Canton, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.name} {self.last_name}'