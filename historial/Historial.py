class Historial:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        historial = self.session.get("historial")
        if not historial:
            self.session["historial"] = {}
            self.historial = self.session["historial"]
        else:
            self.historial = historial

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.historial.keys():
            self.historial[id]={
                "producto_id": producto.id,
                "nombre": producto.nombreProducto,
                "acumulado": producto.precioProducto,
                "cantidad": 1,
            }
        else:
            self.historial[id]["cantidad"] += 1
            self.historial[id]["acumulado"] += producto.precioProducto
        self.guardar_historial()

    def guardar_historial(self):
        self.session["historial"] = self.historial
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.historial:
            del self.historial[id]
            self.guardar_historial()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.historial.keys():
            self.historial[id]["cantidad"] -= 1
            self.historial[id]["acumulado"] -= producto.precioProducto
            if self.historial[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_historial()

    def limpiar(self):
        self.session["historial"] = {}
        self.session.modified = True