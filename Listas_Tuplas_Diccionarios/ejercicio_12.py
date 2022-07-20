"""
12. Utilizando un diccionario. Realizar un programa que permita cargar un código de producto
como llave en un diccionario. Guardar para esta clave el nombre del producto y el precio.
Después de ingresar un producto, preguntar si se desea cargar otro, el límite de productos
lo dispondrá el usuario. Mostrar el listado de productos. Consultar un producto mediante
su clave.
"""


def menu():
    print("""
        ** Menu principal **
        
        1.- Agregar nuevo producto
        2.- Ver listado de productos agregados.
        3.- Salir
    
    """)


# key: Codigo producto
# Value: Nombre y precio del producto
productos = {}


loop = True

while loop:

    menu()
    opc = int(input("Ingrese la opcion de lo que desea realizar: "))
    if opc == 1:
        cod = int(input("Ingrese el codigo de un producto: "))
        desc = input("Ingrese el nombre y valor del producto: ")

        productos[cod] = desc

        print(f"\nSe ha agregado correctamente el producto.\n")

    elif opc == 2:
        print("\nLos productos son:")

        for i in productos:
            print(f"{i} - {productos[i]}")

    elif opc == 3:
        print(f"Los productos agregados son: {productos}")
        print("\nSaliendo del programa.")
        loop = False

    else:
        print("Opcion no valida.")
