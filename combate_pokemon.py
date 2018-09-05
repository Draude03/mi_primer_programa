pokemon_elegido = input("Contra qué pokémon quieres que luche? (Bulbasur / Charmander / Squirtle): ")

#Variables del juego
vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0
ataque_chispazo = 10
ataque_bola_voltio = 12

#Pokemon elegido y sus variables
if pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    ataque_pokemon = 10
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_pokemon = 7
elif pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_pokemon = 8

#Combate
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio): ")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= ataque_chispazo
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= ataque_bola_voltio

    print("La vida de {} es {}".format(pokemon_elegido, vida_enemigo))
    print("{} te hace un ataque de {} de daño".format(pokemon_elegido, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida de tu pikachu es {}".format(vida_pikachu))

#Fin juego
if vida_enemigo <= 0:
    print("Gana tu pikachu")
if vida_pikachu <= 0:
    print(" Gana {}".format(pokemon_elegido))
print("El combate ha terminado")