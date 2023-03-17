from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30,verbose_name='Nombre Completo')
    direccion = models.CharField(max_length=50, verbose_name="La direccion")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        result = f'{self.nombre} | {self.direccion} | {self.email} | {self.telefono}'
        return result

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.FloatField()

    def __str__(self):
        result = f'Nombre: {self.nombre}, Seccion: {self.seccion}, Precio{self.precio}'
        return result


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()    
    entregado = models.BooleanField()

    #def __str__ (self):
    #    result = f'{self.numero}|{self.fecha}|{self.entregado}'
