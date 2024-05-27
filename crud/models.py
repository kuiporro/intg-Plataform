from datetime import time, timedelta
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Donacion(models.Model):
    donacion = models.IntegerField()
    nombreDonante = models.TextField(max_length=20)
    tipoPago = models.IntegerField()

class Usuario(AbstractUser):
    rut = models.TextField(max_length=10)
    dv = models.TextField(max_length=1)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    fechaNac = models.DateField(null=True)
    password = models.CharField(max_length=128)
    email = models.TextField(max_length=30)
    direccion = models.TextField(max_length=30)
    telefono = models.TextField(max_length=12)
    tipoDeUsuario = models.IntegerField(default=0)
    last_login = models.DateField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    username = models.TextField(max_length=20, unique=True)
    suscrito = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.rut

class Boleta(models.Model):
    idBoleta = models.IntegerField()
    username = models.TextField(max_length=20)
    nomProducto = models.TextField(max_length=30)
    cantidad = models.IntegerField()
    estado = models.TextField(max_length=20)
    fecEmision = models.DateField(default=timezone.now)
    fecEntrega = models.DateField(default=(timezone.now() + timedelta(4)))
    direccion = models.TextField(max_length=50)
    total = models.IntegerField()

    def __str__(self):
        return self.username

class Producto(models.Model):
    codigoProducto = models.IntegerField()
    nombreProducto = models.TextField(max_length=100)
    descripcionProducto = models.TextField()
    categoriaProducto = models.IntegerField()
    marcaProducto = models.IntegerField()
    precioProducto = models.IntegerField()
    stockProducto = models.IntegerField()
    precioCosto = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.codigoProducto

class Categoria(models.Model):
    nombreCategoria = models.TextField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreCategoria

class tipoPago(models.Model):
    nombreTipoPago = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreTipoPago

class tipoUsuario(models.Model):
    nombreTipoUsuario = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreTipoUsuario

class Marca(models.Model):
    nombreMarca = models.TextField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreMarca