$(function() // public static void main (JAVa)
{
    $(".btnCreate").click(function()
    {
        let nombre = $(".txtNombre").val();
        if(!nombre){
            alert("Debe especificar el nombre del tipo de pago");
            $(".txtNombre").focus();
            return false;
        }
        else if (nombre.length<5){
            alert("El nombre del tipo de pago debe tener como minimo 5 caracteres");
            $(".txtNombre").focus();
            return false;
        }
        else{
            alert("Tipo de pago registrado correctamente");
        }
    });
    let letras = "qwertyuiopasdfghjklzxcvbnm- ñQWERTYUIOPASDFGHJKLZXCVBNMÑ'";
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
});