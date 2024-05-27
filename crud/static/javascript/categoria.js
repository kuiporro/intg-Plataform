$(function()
{
    $(".btnCreate").click(function()
    {
        let nombre = $(".txtNombre").val();
        if(!nombre){
            alert("Debe especificar el nombre de la categoria");
            $(".txtNombre").focus();
            return false;
        }
        else if (nombre.length<5){
            alert("El nombre de la categoria debe tener como minimo 5 caracteres");
            $(".txtNombre").focus();
            return false;
        }
        else{
            alert("Categoria registrada correctamente");
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