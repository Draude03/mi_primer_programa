"""
Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario
"""

frase_usuario = input("Introduce una frase: ")

vocales = {"a", "e", "i", "o", "u"}
n_vocales = 0

for contar_vocales in frase_usuario:
    if contar_vocales in vocales:
        n_vocales += 1

if n_vocales == 1:
    print("Hay 1 vocal")
else:
    print("Hay {} vocales".format(n_vocales))