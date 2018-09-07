numero_adivinar = input("- Elije un numero para que la otra persona lo adivine (Tiene que ser un numero natural): ")
resultado = 1000000000000000000
import os
os.system("cls")

while resultado != numero_adivinar:
    resultado = input("Adivina el numero: ")

print("¡¡¡Has acertado!!!, el numero era {}".format(numero_adivinar))
