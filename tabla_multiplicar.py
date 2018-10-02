"""
Obtener la tabla de multiplicar de un número especificado por el usuario
"""

numero_tabla = int(input("Introduce un numero del que quieres la tabla de multiplicar: "))

for multiplo in range(1, 11):
        print("{} x {} = {}".format(multiplo, numero_tabla, numero_tabla * multiplo))