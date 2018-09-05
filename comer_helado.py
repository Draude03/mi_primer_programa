apetece_helado_input = input("¿Te apetece un helado? (Si/No)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no")
    apetece_helado = False

if apetece_helado == False:
    print("Pues no hay helado")
    exit()

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si/No)").upper()
esta_tu_tia_input = input("¿Estás con tu tia? (Si/No)").upper()
if tiene_dinero_input == "SI" or esta_tu_tia_input == "SI":
    puedes_permitirtelo = True

else:
    puedes_permitirtelo = False
    print("Pues no hay helado")
    exit()

esta_el_senor_helados_input = input("¿Está el señor de los helados? (Si/No)").upper()
if esta_el_senor_helados_input == "SI":
    esta_el_senor_helados = True
else:
    esta_el_senor_helados = False
    print("Pues no hay helado")
    exit()


if apetece_helado and puedes_permitirtelo and esta_el_senor_helados:
    print("Pues comete un helado")
