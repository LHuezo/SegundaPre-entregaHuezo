from Paquete_Para_Cliente.funct_cliente import Cliente

cliente1=Cliente("Lauty","Huezo",20,500,"MercadoPago")

print(cliente1)

print(cliente1.comprar_producto("Comida",200,"MercadoPago"))

print(cliente1.devuelvo_producto(300,"Comida"))

