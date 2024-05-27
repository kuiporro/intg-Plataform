$(function() // public static void main (JAVa)
{   
    let stock = $('.txtCantidad').text();
    let id = $('.txtId').val();
    let Username = $('.txtUsername').val();
    let direccion = $('.txtDireccion').val();
    let total = $('.Price').val();
    $(".btnCancel").click(function()
    {
        $.getJSON('http://127.0.0.1:8000/api/apiProductoDetalle/'+id+'/', function(data) {
            let producto = data;
            let newStock = parseInt(producto.stockProducto) + parseInt(stock);
            let data2 = {
                "id":producto.id,
                "stockProducto": newStock,
            }
            $.ajax({
                url: 'http://127.0.0.1:8000/api/apiProductoDetalle/'+id+'/',
                method: 'PUT',
                dataType: 'json',
                data: JSON.stringify(data2)
            }).done(function () {
                console.log('SUCCESS');
            }).fail(function (msg) {
                console.log('FAIL');
            });
        }).done(function () {
            console.log('SUCCESS MAIN');
        }).fail(function (msg) {
            console.log('FAIL MAIN');
        });
    });
    $(".btnEnviar").click(function()
    {
        var d = new Date();
        var strDate = d.getFullYear() + "/" + (d.getMonth()+1) + "/" + d.getDate();
        var strDateF = d.getFullYear() + "/" + (d.getMonth()+1) + "/" + (d.getDate()-4);
        alert(strDateF);
        alert(strDate);
        data = {
            'idBoleta':1, 
            'username':Username,
            'estado':"entregado",
            'fecEmision':strDate,
            'fecEntrega':strDateF,
            'direccion':direccion,
            'total':total,
        }
        $.ajax({
            url: 'http://127.0.0.1:8000/api/apiProductoDetalle/'+id+'/',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify(data2)
        }).done(function () {
            console.log('SUCCESS');
        }).fail(function (msg) {
            console.log('FAIL');
        });
    });
});