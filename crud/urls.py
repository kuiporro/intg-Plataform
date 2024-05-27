from django.urls import path
from . import views
urlpatterns = [
    path('tipoPago', views.viewTipoPago, name = "tipoPago"),
    path('tipoPago/<int:id>/', views.viewReadTipoPago, name="tipoPago"),
    path('categoria', views.viewCategoria, name="categoria"),
    path('categoria/<int:id>/', views.viewReadCategoria, name="categoria"),
    path('marca', views.viewMarca, name="marca"),
    path('marca/<int:id>/', views.viewReadMarca, name="marca"),
    path('tipoUsuario', views.viewTipoUsuario, name="tipoUsuario"),
    path('tipoUsuario/<int:id>/', views.viewReadTipoUsuario, name="tipoUsuario"),
    path('producto', views.viewProducto, name="producto"),
    path('producto/<int:id>/', views.viewReadProducto, name="producto"),
    path('usuario', views.viewUsuario, name="usuario"),
    path('usuario/<int:id>/', views.viewReadUsuario, name="usuario"),
    path('historial', views.viewHistorial, name="historial"),
    path('estado', views.viewEstado, name="estado"),
    ]