"""
1.	Diseña un programa que pida por teclado nombres de mascotas y los añada 
    a una lista inicialmente vacía.
    Debe finalizar el ingreso, al preguntar si desea continuar.
	Permita agregar, eliminar y comprobar la existencia de nombres en la lista a solicitud. 
	Muestre la lista resultante.
"""
loop = True
mascotas = []

def menu():
    print("""
        
        Menu de opciones:
        
        1.- Agregar una mascota.
        2.- Eliminar una mascota.
        3.- Ver listado de mascotas almacenadas.
        4.- Salir.         
          
    """)
    
while loop:
    
    menu()
    opc = int(input("¿Que desea realizar?: "))

    if opc == 1:
        mas = True

        while mas:
            add = input("\nIngrese el nombre de su mascota: ")

            mascotas.append(add)
            print("Mascota añadida correctamente!")
            
            other = input("¿Desea agregar otra mascota? - si/no: ")
            
            if other == "no":
                mas = False

        
    elif opc == 2:
        
        if mascotas == []:
            print("No hay ninguna mascota ingresada en el sistema para eliminar")
        
        else:
            for i in mascotas:
                print(i)
                
            delete = input("\nIngrese el nombre de la mascota a eliminar: ")
            
            mascotas.remove(delete)
            print("Mascota eliminada exitosamente!")
    
    elif opc == 3:
        
        print("Las mascotas añadidas en sistema son: \n")
        for i in mascotas:
            print(i)
            
    elif opc == 4:
        loop = False
        
    else:
        print("Opcion ingresada no es valida.")