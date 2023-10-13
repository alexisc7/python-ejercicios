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
def resumen_compra(n,p,c):
    print("Gracias por su compra.\n")
    IVA = 1.21
    precio_total = p * c * IVA
    print(f"Resumen de la compra:\nProducto: {n.capitalize()}\nPrecio unitario: ${p:.2f}\nCantidad de productos a comprar: {c}\nImpuesto IVA(21%): ${(p * c)*0.21:.2f}\nEl precio total a pagar es: ${precio_total:.2f}")

# regresar a la tienda
def return_store(): 
        respuesta = input("desea regresar a la tienda?\n1. Si\n2. No\n:").lower()

        if respuesta == 'si' or respuesta == '1':
            mostrar_productos()
            main()
        elif respuesta == 'no' or respuesta == '2':
            print("Hasta luego :)")
        else:
            print("Ingresaste cualquier mamada. Te crees muy listo? jajaj Pendejo :P")

            last = input("Ultima Chance de comprar tu producto preferido.\nRegresear a la tienda?\n1. Siuu\n2. Niuu\n:").lower()

            if last == '1' or last == 'siuu':
                mostrar_productos()
                main()
            elif last == '2' or last == 'niuu':
                print("Okay :v Hasta nunca bitch")
            else:
                print("Opcion no valida. \nTe dije que era tu ultima chance\npinche pendejo :P\nTa' luego :D")        

# comprar de nuevo
opciones = ['1', 'aceptar', '2', 'cancelar']
def buy_again(): 
        pregunta = input("\n¿Desea comprar otro producto?: \n1. Aceptar\n2. Cancelar\nR: ").lower()
        if pregunta == opciones[0] or pregunta == opciones[1]:
            print("-----------------")
            main()
        elif pregunta == opciones[2] or pregunta == opciones[3]:
            print("hasta luego!")
        else:
            print("Por favor ingrese opcion 1 o 'aceptar' u opcion 2 o 'cancelar")
            return_store()

# ..........
def main():
    nombre_producto = input("\nIngrese el nombre del producto que desea comprar\n:").lower()

    if nombre_producto not in productos_g:
        print("Producto no disponible")
        buy_again()
    elif nombre_producto == "":
        print("No ingreso ningún producto")
    else:
        try: 
            cantidad_producto = int(input("Ingrese la cantidad a comprar\n:")) 
            if cantidad_producto <= 0:
                print("La cantidad de productos no puede ser menor o igual a 0")
            else:
                resumen_compra(nombre_producto, get_precio_usuario(nombre_producto), cantidad_producto)
                buy_again()
        except ValueError:
            print("No ha ingresado una cantidad.")    
            return_store()

if __name__ == "__main__":
    main() 