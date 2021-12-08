from os import system
from classes.game import game

turno = True
xchar = '\033[1m'+'\033[91m'+'x'+'\033[0m'
ochar = '\033[1m'+'\033[94m'+'o'+'\033[0m'
tictac = game()

while(tictac.redflag):
    system("clear")
    tictac.show(tictac.m)

    x = int(input("Ingrese la posicion: "))

    while(x < 1 or x > 9):
        x = int(input("Ingrese una posicion correcta: "))

    h, k = tictac.converpos(x)

    if tictac.m[h][k] != '-':
        print("Posicion llena")
        system("sleep 2")
    else:
        if turno:
            tictac.m[h][k] = xchar
            tictac.show(tictac.m)
            tictac.isWin(tictac.m, xchar)
            turno = False
        else:
            tictac.m[h][k] = ochar
            tictac.show(tictac.m)
            tictac.isWin(tictac.m, ochar)
            turno = True

