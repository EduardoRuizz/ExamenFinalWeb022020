from django.db import models

# Create your models here.


class Producto(models.Model):  
    nombre = models.CharField(max_length=100)  
    precio = models.FloatField() 
    existencia = models.IntegerField() 
    descripcion = models.CharField(max_length=200)

    class Meta:  
        db_table = "Producto"