"""
Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario
"""

frase_usuario = input("Introduce una frase: ")
n_espacios = 0
n_puntos = 0
n_comas = 0



for frase in frase_usuario:
    if frase in " ":
        n_espacios += 1
    elif frase in ".":
        n_puntos += 1
    elif frase in ",":
        n_comas += 1

print("Numero de espacios: {}".format(n_espacios))
print("Numero de puntos: {}".format(n_puntos))
print("Numero de comas: {}".format(n_comas))