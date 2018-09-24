mi_lista = []

input_usuario = ""
input_usuario = input("¿Qué quieres añadir a la lista? (Escribe fin cuando quieras salir): ")

while input_usuario != "Fin":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Qué quieres añadir a la lista? (Escribe fin cuando quieras salir): ")

for item in mi_lista:
    print ("Tengo que comprar {}".format(item))


print("Esta es la lista de la compra")