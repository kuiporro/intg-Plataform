$(function()
{
    $(".btnPagarCarrito").click(function()
    {
        let data = $('.product_id');
        let ids = new Array();
        let amounts = new Array();
        for(let i = 0;i<data.length;i++){
            let x = $(data[i]).html();
            ids.push(x.toString().slice(':')[0]);
            amounts.push(x.toString().slice(':')[2]);
        };
        for(let i = 0;i<data.length;i++){
            let url = 'http://127.0.0.1:8000/remove/'+ids[i]+'/'+amounts[i]+'/';
            $.getJSON('http://127.0.0.1:8000/api/apiProductoDetalle/'+ids[i]+'/', function(data) {
                let producto = data;
                stockProducto = producto.stockProducto;
                if(stockProducto < 1){
                    alert("No queda stock de este producto. ("+producto.nombreProducto+")");
                }
                else if (stockProducto<amounts[i]){
                    alert("No hay stock para la cantidad solicitada. ("+producto.nombreProducto+")");
                }
                else{
                    let newStock = parseInt(producto.stockProducto) - parseInt(amounts[i]);
                    let data = {"id":producto.id,
                            "codigoProducto":producto.codigoProducto,
                            "nombreProducto":producto.nombreProducto,
                            "descripcionProducto":producto.descripcionProducto,
                            "categoriaProducto":producto.categoriaProducto,
                            "marcaProducto":producto.marcaProducto,
                            "precioProducto":producto.precioProducto,
                            "stockProducto": newStock,
                            "precioCosto":producto.precioCosto,
                            "activo":producto.activo
                                }
                    $.ajax({
                        url: 'http://127.0.0.1:8000/api/apiProductoDetalle/'+ids[i]+'/',
                        method: 'PUT',
                        dataType: 'json',
                        data: JSON.stringify(data)}).done(function(){
                            console.log('SUCCESS');
                        }).fail(function (msg) {
                            console.log('FAIL');
                        });
                    
                    $(location).prop('href', url);
                };
            });
        };
    });
});