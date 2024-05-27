from rest_framework import serializers
from crud.models import Donacion, Producto, Usuario, Boleta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Producto
        fields  = [
        'id',
        'stockProducto',
        ]

class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = [
        'id', 
        'donacion', 
        'nombreDonante', 
        'tipoPago'
        ]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
        'username', 
        'suscrito'
        ]

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = [
        'idBoleta', 
        'username',
        'estado',
        'fecEmision',
        'fecEntrega',
        'direccion',
        'total',
        ]