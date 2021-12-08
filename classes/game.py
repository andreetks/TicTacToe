

class game:

    def __init__(self):
        self.redflag = True
        self.m = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]


    def converpos(self,y):
        if y == 1:
            return 0, y - 1
        if y == 2:
            return 0, y - 1
        if y == 3:
            return 0, y - 1
        if y == 4:
            return 1, y - 4
        if y == 5:
            return 1, y - 4
        if y == 6:
            return 1, y - 4
        if y == 7:
            return 2, y - 7
        if y == 8:
            return 2, y - 7
        if y == 9:
            return 2, y - 7

    def show(self, x):  # funcion para mostrar la matriz
        for fila in x:
            for valor in fila:
                print(" ", valor, end=" ")
            print()

    def isDraw(self, x):  # retorna True si todas las celdas estan ocupadas
        drawflag = 0
        for fila in x:
            for valor in fila:
                if valor == '-':
                    drawflag = drawflag+1
        if drawflag == 0:
            return True

    def isWin(self, x, char):
        if x[0][0] == char and x[0][1] == char and x[0][2] == char:
            print("Ganaste ", char)
            self.redflag = False
        elif x[1][0] == char and x[1][1] == char and x[1][2] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[2][0] == char and x[2][1] == char and x[2][2] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[0][0] == char and x[1][0] == char and x[2][0] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[0][1] == char and x[1][1] == char and x[2][1] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[0][2] == char and x[1][2] == char and x[2][2] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[0][0] == char and x[1][1] == char and x[2][2] == char:
            print("Ganaste", char)
            self.redflag = False
        elif x[0][2] == char and x[1][1] == char and x[2][0] == char:
            print("Ganaste", char)
            self.redflag = False
        elif self.isDraw(x):
            print("Empate")
            self.redflag = False
