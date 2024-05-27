$(function() // public static void main (JAVa)
{
    $(".btnEnviar").click(function()
    {
        let Donacion = $(".txtDonacion").val();
        let Pago = $(".cmbMPago").val();
        let Username = $(".txtUser").val();

        if(!Donacion)
        {
            alert("Debe especificar el monto");
            $(".txtDonacion").focus();
            return false;
        }     
        else if(Donacion.length<4){
            alert("El minimo de donacion son: $1.000CLP")
            $(".cmbMPago").focus();
            return false;
        }    
        else if(Pago == 0)
        {
            alert("Debe especificar el medio de pago")
            $(".cmbMPago").focus();
            return false;
        }  
        else{
            let Username = $(".txtUser").val();
            $.getJSON("http://127.0.0.1:8000/api/apiUsuarioDetalle/"+Username+"/", function(getUser) {
                            let usuario = getUser;
                            let data3 = {
                                "username": usuario.username,
                                "suscrito": true
                            }
                        $.ajax({
                            url: "http://127.0.0.1:8000/api/apiUsuarioDetalle/"+Username+"/",
                            method: 'PUT',
                            dataType: 'json',
                            data: JSON.stringify(data3),
                        })
                    }).done(function () {
                        console.log('SUCCESS');
                        $.getJSON('http://127.0.0.1:8000/api/apiDonacion', function(getDonacion) {
                            let donaciones = getDonacion;
                            let newId = (parseInt(donaciones[donaciones.length -1].id));
                            let pagoInt = parseInt(Pago);
                            let donacionInt = parseInt(Donacion);
                            let data4 = {
                                "id":newId,
                                "donacion":donacionInt,
                                "nombreDonante":Username,
                                "tipoPago":pagoInt
                            }
                                $.ajax({
                                    url: "http://127.0.0.1:8000/api/apiDonacion",
                                    method: 'POST',
                                    dataType: 'json',
                                    data: JSON.stringify(data4),
                                })
                        });
                        alert("Se ha suscrito con exito");
                    }).fail(function (msg) {
                        console.log('FAIL');
                    });
        }
    });
    $(".btnDeSus").click(function()
    {
        let Username = $(".txtUser").val();
        $.getJSON("http://127.0.0.1:8000/api/apiUsuarioDetalle/"+Username+"/", function(getUser) {
                        let usuario = getUser;
                        let data3 = {
                            "username": usuario.username,
                            "suscrito": false
                        }
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/apiUsuarioDetalle/"+Username+"/",
                        method: 'PUT',
                        dataType: 'json',
                        data: JSON.stringify(data3),
                    }).done(function () {
                        console.log('SUCCESS');
                        alert("Suscripcion Cancelada");
                    }).fail(function (msg) {
                        console.log('FAIL');
                    });
                }).done(function () {
                    console.log('SUCCESS');
                    alert("Suscripcion Cancelada");
                }).fail(function (msg) {
                    console.log('FAIL');
                });
        });
    let numero = '1234567890';
    $(".txtDonacion").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numero.indexOf(caracter) < 0)
            return false;
    });
});