operar = "Si"
while operar == "Si":

    operacion = input("Qué operación quieres realizar? (Suma, Resta, Multiplicación o División): ")
    num_valores = input("¿Cuántos valores quieres calcular? (2, 3, 4 o 5): ")

    if num_valores == "2":
        valor1 = float(input("Elige el primer valor: "))
        valor2 = float(input("Elige el segundo valor: "))
        if operacion == "Suma":
            resultado = valor1 + valor2
            print("El resultado de la suma es {}".format(resultado))
        elif operacion == "Resta":
            resultado = valor1 - valor2
            print("El resultado de la resta es {}".format(resultado))
        elif operacion == "Multiplicación":
            resultado = valor1 * valor2
            print("El resultado de la multiplicación es {}".format(resultado))
        elif operacion == "División":
            resultado = valor1 / valor2
            print("El resultado de la división es {}".format(resultado))
    elif num_valores == "3":
        valor1 = float(input("Elige el primer valor: "))
        valor2 = float(input("Elige el segundo valor: "))
        valor3 = float(input("Elige el tercer valor: "))
        if operacion == "Suma":
            resultado = valor1 + valor2 + valor3
            print("El resultado de la suma es {}".format(resultado))
        elif operacion == "Resta":
            resultado = valor1 - valor2 - valor3
            print("El resultado de la resta es {}".format(resultado))
        elif operacion == "Multiplicación":
            resultado = valor1 * valor2 * valor3
            print("El resultado de la multiplicación es {}".format(resultado))
        elif operacion == "División":
            resultado = valor1 / valor2 / valor3
            print("El resultado de la división es {}".format(resultado))
    elif num_valores == "4":
        valor1 = float(input("Elige el primer valor: "))
        valor2 = float(input("Elige el segundo valor: "))
        valor3 = float(input("Elige el tercer valor: "))
        valor4 = float(input("Elige el cuarto valor: "))
        if operacion == "Suma":
            resultado = valor1 + valor2 + valor3 + valor4
            print("El resultado de la suma es {}".format(resultado))
        elif operacion == "Resta":
            resultado = valor1 - valor2 - valor3 - valor4
            print("El resultado de la resta es {}".format(resultado))
        elif operacion == "Multiplicación":
            resultado = valor1 * valor2 * valor3 * valor4
            print("El resultado de la multiplicación es {}".format(resultado))
        elif operacion == "División":
            resultado = valor1 / valor2 / valor3 / valor4
            print("El resultado de la división es {}".format(resultado))
    elif num_valores == "5":
        valor1 = float(input("Elige el primer valor: "))
        valor2 = float(input("Elige el segundo valor: "))
        valor3 = float(input("Elige el tercer valor: "))
        valor4 = float(input("Elige el cuarto valor: "))
        valor5 = float(input("Elige el quinto valor: "))
        if operacion == "Suma":
            resultado = valor1 + valor2 + valor3 + valor4 + valor5
            print("El resultado de la suma es {}".format(resultado))
        elif operacion == "Resta":
            resultado = valor1 - valor2 - valor3 - valor4 - valor5
            print("El resultado de la resta es {}".format(resultado))
        elif operacion == "Multiplicación":
            resultado = valor1 * valor2 * valor3 * valor4 * valor5
            print("El resultado de la multiplicación es {}".format(resultado))
        elif operacion == "División":
            resultado = valor1 / valor2 / valor3 / valor4 / valor5
            print("El resultado de la división es {}".format(resultado))
    operar = input("¿Quieres hacer otra operacion? (Si / No)")

