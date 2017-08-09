from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=255)
    telefono = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
