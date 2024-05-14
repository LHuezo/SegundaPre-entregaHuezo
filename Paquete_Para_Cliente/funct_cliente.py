
class Cliente():
    def __init__(self,name,secondane,age,cant_dinero,metodo_de_pago):
        self.nombre=name
        self.apellido=secondane
        self.edad=age
        self.dinero=cant_dinero
        self.medio=metodo_de_pago
        
    def __str__(self):
        return f"Hola, mi nombre es {self.nombre},mi apellido es {self.apellido},tengo {self.edad} años,tengo como medio de pago {self.medio}"
    
    def comprar_producto(self,producto,precio,metodo):
        if metodo == self.medio:
            if self.dinero < precio:
                return f"No tengo suficiente dinero para comprar el producto {str(producto)}"
            else:
                self.dinero -= precio
                return f"Mi dinero fue suficente para comprar el producto {producto} ahora tengo {self.dinero} peso/s restantes"
        else:
            return f"Mi metodo de pago {self.medio} no es el esperado"
        
    def devuelvo_producto(self,precio,producto):
        self.dinero+=precio
        return f"He podido devolver el producto {producto} y ahora tengo {self.dinero} peso/s"
    
