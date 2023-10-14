productos = {
    "instrumentos_musicales": {
        "guitarra": 1200,
        "bateria": 1700,
        "piano": 2500,
        "bajo": 1250,
        "trompeta": 1100,
        "saxofon": 1300,
        "guitarra electrica": 1400
    },
    "electrodomesticos": {
        "heladera": 1900,
        "microondas": 720,
        "ventilador": 900,
        "aire acondicionado": 1100,
        "calefactor": 650,
        "smart tv": 1350,
        "smartphone": 750,
        "notebook": 1500,
        "cafetera": 680
    }
}

# lista de productos disponibles (solo los productos, sin sus precios).
productos_g = [] 

compras_realizadas = {}

# Mostrar categorías y productos
def mostrar_productos():
    print("Bienvenido a la tienda\n\nProductos con sus respectivos precios:")
    for categoria, productos_en_categoria in productos.items():
        print(f"\nCategoría: {categoria.capitalize()}")
        for producto, precio in productos_en_categoria.items():
            print(f"{producto.capitalize()}: {precio}")
            productos_g.append(producto.lower()) # agrega los productos a la lista 'productos_g'

mostrar_productos()

# obtener precio del producto elegido por el usuario
def get_precio_usuario(nom_prod):
    vista_dict = productos.items()
    for _, productos_en_categoria in vista_dict:
        for producto, precio in productos_en_categoria.items():
            if nom_prod == producto:
                precio_unidad = precio 
                break
    return precio_unidad


# generar resumen de compra
def resumen_compra(nombre_prod,precio,cantidad):
    if nombre_prod in compras_realizadas:
        compras_realizadas[nombre_prod]["cantidad"] += cantidad
    else:
        compras_realizadas[nombre_prod] = {"precio_unitario": precio, "cantidad": cantidad}


def compra_total():
    IVA = 1.21
    total_con_IVA = 0
    for _, detalles in compras_realizadas.items():
        precio_unitario = detalles["precio_unitario"]
        cantidad = detalles["cantidad"]
        total_IVA = precio_unitario * cantidad * IVA

        total_con_IVA+=total_IVA
    print(f"Total de las compras realizadas (IVA incluido): ${total_con_IVA:.2f}\nGracias por su compra.\nHasta luego!")


def mostrar_resumen():
    IVA = 1.21
    print("\nResumen de las compras realizadas:")
    for producto, detalles in compras_realizadas.items():
        precio_unitario = detalles["precio_unitario"]
        cantidad = detalles["cantidad"]
        total = precio_unitario * cantidad
        total_IVA = precio_unitario * cantidad * IVA
        print(f"  Producto: {producto.capitalize()}\n  Precio unitario: ${precio_unitario:.2f}\n  Cantidad: {cantidad}\n  Impuesto IVA(21%): ${total*0.21:.2f}\n  Total de esta compra (IVA incluido): ${total_IVA:.2f}\n-----------------")


def verificar_compras():
    if compras_realizadas == {}:
        print("No ha realizado ninguna compra.\nHasta luego!")
    elif len(list(compras_realizadas.keys())) > 1:
        mostrar_resumen()
        compra_total() 
    else:
        mostrar_resumen()
        print("Gracias por su compra.\nHasta luego!")



# regresar a la tienda
def return_store(): 
    respuesta = input("desea regresar a la tienda?\n1. Si\n2. No\n:").lower()

    if respuesta == 'si' or respuesta == '1':
        mostrar_productos()
        main()
    elif respuesta == 'no' or respuesta == '2':
        verificar_compras()
    else:
        print("Opción no valida")

        last = input("Ultima chance de comprar su producto preferido.\nRegresear a la tienda?\n1. Si\n2. No\n:").lower()

        if last == '1' or last == 'si':
            mostrar_productos()
            main()
        elif last == '2' or last == 'no':
            verificar_compras()
        else:
            print("Opción ingresada no valida")  
            verificar_compras()      

# comprar de nuevo
opciones = ['1', 'aceptar', '2', 'cancelar']
def buy_again(): 
    pregunta = input("\n¿Desea comprar otro producto?: \n1. Aceptar\n2. Cancelar\nR: ").lower()
    if pregunta == opciones[0] or pregunta == opciones[1]:
        print("-----------------")
        main()
    elif pregunta == opciones[2] or pregunta == opciones[3]:
        verificar_compras()
    else:
        print("Por favor ingrese opcion 1 o 'aceptar' u opcion 2 o 'cancelar")
        return_store()
        
# ..........
def main():
    nombre_producto = input("\nIngrese el nombre del producto que desea comprar\n:").lower()

    if nombre_producto == "":
        print("No ingreso ningún producto")
        return_store()
    elif nombre_producto not in productos_g:
        print("Producto no disponible")
        buy_again()
    else:
        try: 
            cantidad_producto = int(input("Ingrese la cantidad a comprar\n:")) 
            if cantidad_producto <= 0:
                print("La cantidad de productos no puede ser menor o igual a 0")
                return_store()
            else:
                resumen_compra(nombre_producto, get_precio_usuario(nombre_producto),cantidad_producto)
                buy_again()
        except ValueError:
            print("No ha ingresado una cantidad.")    
            return_store()

if __name__ == "__main__":
    main() 