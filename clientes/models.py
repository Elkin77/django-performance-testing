from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.IntegerField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    