from django.contrib import admin
from .models import Categoria, Producto, Usuario, tipoPago, tipoUsuario, Marca
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(tipoPago)
admin.site.register(tipoUsuario)
admin.site.register(Producto)
admin.site.register(Usuario, UserAdmin)