from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Categoria, Marca, Usuario, tipoPago, tipoUsuario, Producto
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from crud.models import Producto

@login_required
def viewEstado(request):
    cntx = {}
    return render(request, 'estado.html', cntx)

@login_required
@permission_required('is_superuser')    
def viewTipoPago(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreTipoPago = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreTipoPago) < 5:
                cntx = {'error': 'El nombre del tipo de pago debe tener como minimo 5 caracteres'}
            elif id < 1:
                tipoPago.objects.create(nombreTipoPago = nombreTipoPago, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = tipoPago.objects.get(pk = id)
                fila.nombreTipoPago = nombreTipoPago
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = tipoPago.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen Tipos de Pagos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = tipoPago.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoPago.html', cntx)
    

@login_required
@permission_required('is_superuser')
def viewReadTipoPago(request, id):
    cntx = {}
    try:
        fila = tipoPago.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoPago.html', cntx)

@login_required
@permission_required('is_superuser')
def viewCategoria(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreCategoria = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreCategoria) < 5:
                cntx = {'error': 'El nombre de la categoria debe tener como minimo 5 caracteres'}
            elif id < 1:
                Categoria.objects.create(nombreCategoria = nombreCategoria, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Categoria.objects.get(pk = id)
                fila.nombreCategoria = nombreCategoria
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Categoria.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen Categorias para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Categoria.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'categoria.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadCategoria(request, id):
    cntx = {}
    try:
        fila = Categoria.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'categoria.html', cntx)

def viewTipoUsuario(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreTipoUsuario = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreTipoUsuario) < 5:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif id < 1:
                tipoUsuario.objects.create(nombreTipoUsuario = nombreTipoUsuario, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = tipoUsuario.objects.get(pk = id)
                fila.nombreTipoUsuario = nombreTipoUsuario
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = tipoUsuario.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen tipos de usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = tipoUsuario.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoUsuario.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadTipoUsuario(request, id):
    cntx = {}
    try:
        fila = tipoUsuario.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoUsuario.html', cntx)


@login_required
@permission_required('is_superuser')
def viewProducto(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        codigoProducto = request.POST["txtCode"]
        nombreProducto = request.POST["txtNombre"]
        descripcionProducto = request.POST["txtDesc"]
        categoriaProducto = request.POST["ctProducto"]
        marcaProducto = request.POST["ctMarca"]
        precioProducto = request.POST["txtPrecio"]
        stockProducto = request.POST["txtStock"]
        precioCosto = request.POST["txtCosto"]
        imgFlag = False
        activo = False
        if 'img' in request.FILES:
            img = request.FILES['img']
            fs = FileSystemStorage()
            img = fs.save(img.name, img)
        else:
            imgFlag = True
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(codigoProducto) < 5:
                cntx = {'error': 'El codigo del producto debe tener como minimo 5 caracteres'}
            elif len(nombreProducto) < 5:
                cntx = {'error': 'El nombre del producto debe tener como minimo 5 caracteres'}
            elif len(descripcionProducto) < 10:
                cntx = {'error': 'La descripcion del producto debe tener como minimo 10 caracteres'}
            elif (categoriaProducto) == '0':
                cntx = {'error': 'Debe seleccionar la categoria del producto'}
            elif (marcaProducto) == '0':
                cntx = {'error': 'Debe seleccionar la marca del producto'}
            elif len(precioProducto) < 3:
                cntx = {'error': 'El precio del producto debe ser mayor a 500'}
            elif (int(precioProducto)) < 500:
                cntx = {'error': 'El precio del producto debe ser mayor a 500'}
            elif (int(stockProducto)) < 1:
                cntx = {'error': 'El stock del producto debe ser mayor a 0'}
            elif len(precioCosto) < 3:
                cntx = {'error': 'El costo del producto debe ser mayor a 500'}
            elif (int(precioCosto)) < 500:
                cntx = {'error': 'El costo del producto debe ser mayor a 500'}
            elif imgFlag:
                cntx = {'error': 'Debe especificar la imagen del producto'}
            elif id < 1:
                Producto.objects.create(codigoProducto = codigoProducto, nombreProducto = nombreProducto, descripcionProducto = descripcionProducto, categoriaProducto = categoriaProducto, marcaProducto = marcaProducto, precioProducto = precioProducto, stockProducto = stockProducto, precioCosto = precioCosto, imagen = img, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Producto.objects.get(pk = id)
                fila.codigoProducto = codigoProducto
                fila.nombreProducto = nombreProducto
                fila.descripcionProducto = descripcionProducto
                fila.categoriaProducto = categoriaProducto
                fila.marcaProducto = marcaProducto
                fila.precioProducto = precioProducto
                fila.stockProducto = stockProducto
                fila.precioCosto = precioCosto
                fila.activo = activo
                fila.imagen = img
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Producto.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen productos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Producto.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}

    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    cntx["productCategories"] = productCategories
    cntx["productBrand"] = productBrand

    return render(request, 'producto.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadProducto(request, id):
    cntx = {}
    try:
        fila = Producto.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    cntx["productCategories"] = productCategories
    cntx["productBrand"] = productBrand
    return render(request, 'producto.html', cntx)

@login_required
@permission_required('is_superuser')
def viewUsuario(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        rut = request.POST["txtRut"]
        dv = request.POST["txtDV"]
        username = request.POST["txtUsername"]
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        fechaNac = request.POST["fecNac"]
        raw_password = request.POST["txtPassword"]
        password = make_password(raw_password, salt=None, hasher='default')
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        telefono = request.POST["txtTel"]
        tipoDeUsuario = request.POST["cmbTipoUsuario"]
        if (tipoDeUsuario == '1'):
            is_super = True
            is_staff = True
        else:
            is_super = False
            is_staff = False
        if 'btnCreate' in request.POST:
            if len(rut)<8:
                cntx = {'error': 'El rut del usuario debe tener como minimo 8 caracteres'}
            elif len(dv)<1:
                cntx = {'error': 'Debe especificar el digito verificador'}
            elif len(username) < 3:
                cntx = {'error': 'El nombre de usuario debe tener como minimo 3 caracteres'}
            elif len(nombre) < 3:
                cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(apellido) < 3:
                cntx = {'error': 'El apellido del usuario debe tener como minimo 3 caracteres'}
            # elif len(fechaNac) < 3:
            #     cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(raw_password) < 8:
                cntx = {'error': 'La contraseña del usuario debe tener como minimo 8 caracteres'}
            elif len(email) < 8:
                cntx = {'error': 'El correo del usuario debe tener como minimo 8 caracteres'}
            elif len(direccion) < 8:
                cntx = {'error': 'La direccion del usuario debe tener como minimo 8 caracteres'}
            elif len(telefono) < 8:
                cntx = {'error': 'El telefono del usuario debe tener como minimo 8 caracteres'}
            elif tipoDeUsuario == '0':
                cntx = {'error': 'Debe seleccionar un tipo de usuario'}
            elif id < 1:
                password = make_password(raw_password, salt=None, hasher='default')
                Usuario.objects.create(rut = rut , dv = dv, username = username, first_name = nombre, last_name = apellido, fechaNac = fechaNac, password = password, email = email, direccion = direccion, telefono = telefono, tipoDeUsuario = tipoDeUsuario, is_superuser = is_super, is_staff = is_staff)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                usuario = Usuario.objects.get(pk = id)
                usuario.rut = rut
                usuario.dv = dv
                usuario.username = username
                usuario.first_name = nombre
                usuario.last_name = apellido
                usuario.fechaNac = fechaNac
                usuario.password = password
                usuario.email = email
                usuario.direccion = direccion
                usuario.telefono = telefono
                usuario.tipoDeUsuario = tipoDeUsuario
                usuario.is_superuser = is_super
                usuario.is_staff = is_staff
                usuario.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Usuario.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen productos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                usuario = Usuario.objects.get(pk = id)
                usuario.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    userCategories = tipoUsuario.objects.all()
    cntx['userCategories'] = userCategories

    return render(request, 'usuario.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadUsuario(request, id):
    cntx = {}
    try:
        fila = Usuario.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    userCategories = tipoUsuario.objects.all()
    cntx['userCategories'] = userCategories
    return render(request, 'usuario.html', cntx)

@login_required
@permission_required('is_superuser')
def viewMarca(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreMarca) < 4:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif id < 1:
                Marca.objects.create(nombreMarca = nombreMarca, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Marca.objects.get(pk = id)
                fila.nombreMarca = nombreMarca
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Marca.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen tipos de usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'marca.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadMarca(request, id):
    cntx = {}
    try:
        fila = Marca.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'marca.html', cntx)

def viewCliente(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        rut = request.POST["txtRut"]
        dv = request.POST["txtDV"]
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        fechaNac = request.POST["fecNac"]
        password = request.POST["txtPassword"]
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        username = request.POST["txtUsername"]
        telefono = request.POST["txtTel"]
        raw_password = request.POST["txtPassword"]
        password = make_password(raw_password, salt=None, hasher='default')
        if 'btnCreate' in request.POST:
            if len(rut)<8:
                cntx = {'error': 'El rut del usuario debe tener como minimo 8 caracteres'}
            elif len(dv)<1:
                cntx = {'error': 'Debe especificar el digito verificador'}
            elif len(nombre) < 3:
                cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(apellido) < 3:
                cntx = {'error': 'El apellido del usuario debe tener como minimo 3 caracteres'}
            # elif len(fechaNac) < 3:
            #     cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(password) < 8:
                cntx = {'error': 'La contraseña del usuario debe tener como minimo 8 caracteres'}
            elif len(email) < 8:
                cntx = {'error': 'El correo del usuario debe tener como minimo 8 caracteres'}
            elif len(direccion) < 8:
                cntx = {'error': 'La direccion del usuario debe tener como minimo 8 caracteres'}
            elif len(telefono) < 8:
                cntx = {'error': 'El telefono del usuario debe tener como minimo 8 caracteres'}
            elif id < 1:
                Usuario.objects.create(rut = rut , dv = dv, first_name = nombre, last_name = apellido, fechaNac = fechaNac, password = password, email = email, direccion = direccion, telefono = telefono, username = username, tipoDeUsuario = 2)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Usuario.objects.get(pk = id)
                fila.rut = rut
                fila.dv = dv
                fila.first_name = nombre
                fila.last_name = apellido
                fila.fechaNac = fechaNac
                fila.password = password
                fila.email = email
                fila.direccion = direccion
                fila.telefono = telefono
                fila.tipoDeUsuario = 3
                fila.username = username
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'cliente.html', cntx)

@login_required
@permission_required('is_superuser')
def viewApi(request):
    cntx = {}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'api.html', cntx)

def viewLogin(request):
    cntx = {}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'login.html', cntx)

def viewReset(request):
    cntx = {}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'reset.html', cntx)

def viewInicio(request):
    cntx = {}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'inicio.html', cntx)

def viewHistorial(request):
    cntx = {}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'historial.html', cntx)

@login_required
def viewDonar(request):
    # if request.method == "POST":
    #     if "btnDonar" in request.POST:

    cntx = {}
    payCategories = tipoPago.objects.all()
    cntx["payCategories"] = payCategories
    return render(request, 'donar.html', cntx)

def viewProductos(request):
    cntx = {}
    products = Producto.objects.all()
    cntx["products"] = products
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'productos.html', cntx)

def viewDetalleProductos(request, id):
    cntx = {}
    try:
        fila = Producto.objects.get(pk = id)
        cntx = {'fila':fila}
    except:
        cntx = {'error': 'Producto no encontrado'}
    products = Producto.objects.all()
    cntx["products"] = products
    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    cntx["productCategories"] = productCategories
    cntx["productBrand"] = productBrand

    return render(request, 'detalleProducto.html', cntx)