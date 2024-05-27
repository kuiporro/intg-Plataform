"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud import views
from shopyCart.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto, restar_producto_n
from historial.views import h_agregar_producto, h_eliminar_producto, h_limpiar_historial, h_restar_producto, h_restar_producto_n
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.viewApi, name="api"),
    path('signin', views.viewCliente, name="signin"),
    path('login', views.viewLogin, name="login"),
    path('reset', views.viewReset, name="reset"),
    path('', views.viewInicio, name="inicio"),
    path('donar', views.viewDonar, name="donar"),
    path('productos', views.viewProductos, name="productos"),
    path('productos/<int:id>/', views.viewDetalleProductos, name="detalleProductos"),
    path('crud/', include('crud.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/<int:producto_id>/', agregar_producto, name="Add"),
    path('remove/<int:producto_id>/', restar_producto, name="Sub"),
    path('remove/<int:producto_id>/<int:n>/', restar_producto_n, name="SubN"),
    path('delete/<int:producto_id>/', eliminar_producto, name="Del"),
    path('clear/', limpiar_carrito, name="CLS"),
    path('historialAdd/<int:producto_id>/', h_agregar_producto, name="HAdd"),
    path('historialRemove/<int:producto_id>/', h_restar_producto, name="HSub"),
    path('historialRemove/<int:producto_id>/<int:n>/', h_restar_producto_n, name="HSubN"),
    path('historialDelete/<int:producto_id>/', h_eliminar_producto, name="HDel"),
    path('historialClear/', h_limpiar_historial, name="HCLS"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)