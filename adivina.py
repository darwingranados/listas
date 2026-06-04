import random

def tirar_dados():
    return random.randint(2, 12)

def pedir_respuesta():
    print("ingresa tu prediccion")
    print("1: par")
    print("2: impar")
    print("salir del juego")

    return int(input())
