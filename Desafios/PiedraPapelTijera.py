from random import randint

opciones = ["Piedra", "Papel", "Tijera"]
valor_aleatorio = randint(0,2)
juego_computador = opciones[valor_aleatorio]

juego_usuario = input("¿Qué elije? Piedra, Papel, Tijera ")

if juego_usuario == juego_computador:
    print("¡Es un Empate!")
elif juego_usuario == "Piedra":
    if juego_computador == "Papel":
        print("¡Perdiste!", juego_computador, "cubre", juego_usuario)
    else:
        print("¡Ganaste!", juego_usuario, "aplasta", juego_computador)
elif juego_usuario == "Papel":
    if juego_computador == "Tijera":
        print("¡Perdiste!", juego_computador, "corta", juego_usuario)
    else:
        print("¡Ganaste!", juego_usuario, "cubre", juego_computador)
elif juego_usuario == "Tijera":
    if juego_computador == "Piedra":
        print("¡Perdiste!", juego_computador, "aplasta", juego_usuario)
    else:
        print("¡Ganaste!", juego_usuario, "corta", juego_computador)
else:
    print("Palabra no valida")