from django.db import models

# Create your models here.

class Foto(models.Model):
    nombre = models.CharField(blank="", null=True, max_length=15)
    apellido = models.CharField(blank="", null=True, max_length=15)
    fecha_creacion = models.DateField(auto_created=True)

    #para definir el nombre en la bd
    def __str__(self): #este es un metodo de cero parameteos (this)
        return self.nombre







