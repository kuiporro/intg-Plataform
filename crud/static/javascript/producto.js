$(function()
{
    $(".btnCreate").click(function()
    {
        let code = $(".txtCode").val();
        let nombre = $(".txtNombre").val();
        let desc = $(".txtDesc").val();
        let precio = $(".txtPrecio").val();
        let stock = $(".txtStock").val();
        let categoria = $('.ctProducto').val();
        let marca = $('.ctMarca').val();
        let costo = $('.txtCosto').val();
        let img = $('.img').val();
        if(!code){
            alert("Debe especificar el codigo del producto");
            $(".txtCode").focus();
            return false;
        }
        else if(code.length < 5){
            alert("El codigo del producto debe tener como minimo 5 caracteres");
            $(".txtCode").focus();
            return false;
        }
        else if(!nombre){
            alert("Debe especificar el nombre del producto");
            $(".txtNombre").focus();
            return false;
        }
        else if(nombre.length < 5){
            alert("El nombre del producto debe tener como minimo 5 caracteres");
            $(".txtNombre").focus();
            return false;
        }
        else if(!desc){
            alert("Debe especificar la descripción del producto");
            $(".txtDesc").focus();
            return false;
        }
        else if(desc.length < 10){
            alert("La descripción del producto debe tener como minimo 10 caracteres");
            $(".txtDesc").focus();
            return false;
        }
        else if (categoria == '0'){
            alert("Debe especificar la categoria del producto")
            $(".ctProducto").focus();
            return false;
        }
        else if (marca == '0'){
            alert("Debe especificar la marca del producto")
            $(".ctMarca").focus();
            return false;
        }
        else if(!precio){
            alert("Debe especificar el precio del producto");
            $(".txtPrecio").focus();
            return false;
        }
        else if(precio<500){
            alert("El precio minimo debe ser de 500 pesos");
            $(".txtPrecio").focus();
            return false;
        }
        else if(!stock){
            alert("Debe especificar el stock del producto");
            $(".txtStock").focus();
            return false;
        }
        else if(stock<1){
            alert("El numero de stock debe ser mayor que 0");
            $(".txtStock").focus();
            return false;
        }
        else if(!costo){
            alert("Debe especificar el costo del producto");
            $(".txtCosto").focus();
            return false;
        }
        else if(costo<500){
            alert("El precio minimo del costo deber ser de 500 pesos");
            $(".txtCosto").focus();
            return false;
        }
        else if(parseInt(costo)>parseInt(precio)){
            alert("El costo deber ser menor que el precio del producto");
            $(".txtCosto").focus();
            return false;
        }
        else if(!img){
            alert("Debe especificar la imagen del producto");
            $(".img").focus();
            return false;
        }
        else{
            alert("Producto registrado correctamente")
        }
    });
    let numeros = '1234567890';
    $(".txtCode").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    let letras = "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890' ";
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtDesc").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtPrecio").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
    $(".txtStock").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
});