print("#####################################")
print("# Conversor de fahrenheit a celcius #")
print("#####################################")

grados_convertir = float(input("Escribe los grados en fahrenheit para convertirlos en celcius: "))

resultado = float((grados_convertir - 32) / 1.8)

print("{}ºF en celcius son {}ºC".format(grados_convertir, resultado))

