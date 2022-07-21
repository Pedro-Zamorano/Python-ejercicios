"""
Diccionarios
3.	Haga un programa que solicite nombre de usuario y contraseña. Haga las siguientes validaciones:
	El nombre de usuario debe estar en minúscula.
	La contraseña debe contener al menos 8 caracteres. 
	No debe quedar en blanco ninguno de los dos datos solicitados.
	Solo se pueden ingresar valores alfanuméricos.
"""

loop = True
data = {}

while loop:
    user = input("Usuario: ")
    passwd = input("Contraseña: ")

    if user:
        print(user)
        
    elif len(passwd) < 1 or len(passwd) > 8:
        print(passwd)

