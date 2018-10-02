"""
Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario pero invertida, comenzando desde el 10.
"""

numero_tabla = int(input("Introduce un numero del que quieres la tabla de multiplicar: "))

for multiplo in reversed(range(1, 11)):
        print("{} x {} = {}".format(multiplo, numero_tabla, numero_tabla * multiplo))