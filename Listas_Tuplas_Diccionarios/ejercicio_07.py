"""
7. Crea una tupla con los meses del año. Ingresa un número por teclado y muestra el mes
asociado, en caso contrario, muestra un mensaje de error.
"""

month = ('', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
         'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

selectMonth = int(input('Ingrese un numero para mostrar el mes (del 1 al 12): '))

if selectMonth <= 0 or selectMonth > 12:
    print("\nNumero ingresado esta fuera de rango")

else:
    print(f"\n{month[selectMonth]}")



