import os

m = [['-', '-', '-'],
     ['-', '-', '-'],
     ['-', '-', '-']]

redflag = True
turno = True
xchar = '\033[1m'+'\033[91m'+'x'+'\033[0m'
ochar = '\033[1m'+'\033[94m'+'o'+'\033[0m'


def convertirpos(y):
    if y <= 3:
        if y == 1:
            return 0, y - 1
        if y == 2:
            return 0, y - 1
        if y == 3:
            return 0, y - 1
    elif y <= 6:
        y = y - 3
        if y == 1:
            return 1, y - 1
        if y == 2:
            return 1, y - 1
        if y == 3:
            return 1, y - 1
    elif y > 6:
        y = y - 6
        if y == 1:
            return 2, y - 1
        if y == 2:
            return 2, y - 1
        if y == 3:
            return 2, y - 1


def show(x):  # funcion para
    for fila in x:
        for valor in fila:
            print(" ", valor, end=" ")
        print()


def isDraw(x):  # retorna True si todas las celdas estan ocupadas
    drawflag = 0
    for fila in x:
        for valor in fila:
            if valor == '-':
                drawflag = drawflag+1
    if drawflag == 0:
        return True


def isWin(x, char):
    global redflag
    if x[0][0] == char and x[0][1] == char and x[0][2] == char:
        print("Ganaste ", char)
        redflag = False
    if x[1][0] == char and x[1][1] == char and x[1][2] == char:
        print("Ganaste", char)
        redflag = False
    if x[2][0] == char and x[2][1] == char and x[2][2] == char:
        print("Ganaste", char)
        redflag = False
    if x[0][0] == char and x[1][0] == char and x[2][0] == char:
        print("Ganaste", char)
        redflag = False
    if x[0][1] == char and x[1][1] == char and x[2][1] == char:
        print("Ganaste", char)
        redflag = False
    if x[0][2] == char and x[1][2] == char and x[2][2] == char:
        print("Ganaste", char)
        redflag = False
    if x[0][0] == char and x[1][1] == char and x[2][2] == char:
        print("Ganaste", char)
        redflag = False
    if x[0][2] == char and x[1][1] == char and x[2][0] == char:
        print("Ganaste", char)
        redflag = False
    if isDraw(x):
        print("Empate")
        redflag = False


while(redflag):
    os.system("clear")
    show(m)

    x = int(input("Ingrese la posicion: "))

    while(x < 1 or x > 9):
        x = int(input("Ingrese una posicion correcta: "))

    h, k = convertirpos(x)

    if m[h][k] != '-':
        print("Posicion llena")
        os.system("sleep 2")
    else:
        if turno:
            m[h][k] = xchar
            show(m)
            isWin(m, xchar)
            turno = False
        else:
            m[h][k] = ochar
            show(m)
            isWin(m, ochar)
            turno = True


# prueba
