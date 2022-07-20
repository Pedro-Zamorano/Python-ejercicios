"""
4. Diseña un programa que pida por teclado los nombres de personas y los añada a una lista
inicialmente vacía y además que de la posibilidad de eliminarlos cuando se solicite.
Terminada la acción el programa preguntará si se desea continuar introduciendo o
eliminado nuevos nombres. Cuando el usuario responda que no, el programa se detendrá.

5. Modifica el programa del ejercicio anterior para que, a continuación, muestre los datos de
la lista.

"""
nameList = []


def continueOpc():
    print("¿Desea realizar otra operacion? - SI / NO")
    opc = input("> ")

    if opc == 'NO' or opc == 'no':
        exit()


def add():
    newName = input("\nIngrese el nombre: ")
    nameList.append(newName)

    return nameList, continueOpc()


def delete():
    print("\n******************************")
    print(f"Los nombres actuales son: ")
    for i in nameList:
        print(i)
    print("******************************\n")

    lessName = input("Ingrese el nombre a eliminar: ")
    nameList.remove(lessName)

    return nameList, continueOpc()


while True:
    if len(nameList) == 0:
        print("")
    else:
        print("El listado actual de personas es: ")
        for i in nameList:
            print(i)

    print("""
    *******************************************
    **** Bienvenido al menú ****
        Que accion desea realizar:
        
        1.- Ingresar nuevos nombres.
        2.- Eliminar nombres.
    
    """)
    opc = int(input("\nIngese su opción: "))

    if opc == 1:
        add()

    elif opc == 2:
        if len(nameList) == 0:
            print("\nNo hay datos para eliminar.")

        else:
            delete()

    else:
        print("\nOpcion invalida\n")


