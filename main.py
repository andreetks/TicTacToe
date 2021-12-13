from classes.game import game
from os import system


running = True

def menu():
    print("\t\tMENU")
    print("1. Ingresar Jugadores")
    print("2. Jugar")
    print("3. Ver Marcador")
    print("0. Salir")

while(running):
    system("clear")
    menu()
    opc=int(input("Ingresar opcion->"))
    if opc == 0:
        system("clear")
        running = False
    elif opc == 1:
        jugador1 = input("Ingresar el nombre del primer jugador: ")
        jugador2 = input("Ingresar el nombre del segundo jugador: ")
        system("sleep 2")
    elif opc == 2:
        jugador1 = input("Ingresar el nombre del primer jugador: ")
        jugador2 = input("Ingresar el nombre del segundo jugador: ")
        tictac = game(jugador1,jugador2)
        tictac.initgame()
        system("sleep 2")
    elif opc == 3:
        system("clear")
        print("Jugadores gg:\n1.Gillipollas\n2.Tonto")
        system("sleep 2")
    




