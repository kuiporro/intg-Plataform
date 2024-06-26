# Generated by Django 4.0.5 on 2023-06-29 09:06

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
from datetime import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBoleta', models.IntegerField()),
                ('username', models.TextField(max_length=20)),
                ('nomProducto', models.TextField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('estado', models.TextField(max_length=20)),
                ('fecEmision', models.DateField(default=django.utils.timezone.now)),
                ('fecEntrega', models.DateField(default=datetime.datetime(2023, 7, 3, 9, 6, 5, 603429, tzinfo=timezone.utc))),
                ('direccion', models.TextField(max_length=50)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.TextField(max_length=100)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donacion', models.IntegerField()),
                ('nombreDonante', models.TextField(max_length=20)),
                ('tipoPago', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMarca', models.TextField(max_length=50)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.IntegerField()),
                ('nombreProducto', models.TextField(max_length=100)),
                ('descripcionProducto', models.TextField()),
                ('categoriaProducto', models.IntegerField()),
                ('marcaProducto', models.IntegerField()),
                ('precioProducto', models.IntegerField()),
                ('stockProducto', models.IntegerField()),
                ('precioCosto', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Productos')),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoPago', models.TextField()),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoUsuario', models.TextField()),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.TextField(max_length=10)),
                ('dv', models.TextField(max_length=1)),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('fechaNac', models.DateField(null=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.TextField(max_length=30)),
                ('direccion', models.TextField(max_length=30)),
                ('telefono', models.TextField(max_length=12)),
                ('tipoDeUsuario', models.IntegerField(default=0)),
                ('last_login', models.DateField(default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('username', models.TextField(max_length=20, unique=True)),
                ('suscrito', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
