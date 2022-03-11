# Importing Custom Modules
from defs import *
from building import Building

class Game:
    def __init__(self):
        # Initializing vars
        self.board = []
        self.state = True
        self.activeBuildings = []

        # Calling init functions
        self.initBoard()
        self.initTH()
        self.initHut()

    def initBoard(self):
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                if(i == 0 and j == 0):
                    row.append(TOP_LEFT_CORNER)
                elif(i == 0 and j == COLS-1):
                    row.append(TOP_RIGHT_CORNER)
                elif(i == ROWS-1 and j == 0):
                    row.append(BOTTOM_LEFT_CORNER)
                elif(i == ROWS-1 and j == COLS-1):
                    row.append(BOTTOM_RIGHT_CORNER)
                elif(i == 0 or i == ROWS-1):
                    row.append(TOP_WALLS)
                elif(j == 0 or j == COLS-1):
                    row.append(SIDE_WALLS)
                else:
                    row.append(BG)
            row.append('\n')
            self.board.append(row)
    
    def printBoard(self):
        board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end='')

    def initTH(self):
        TH = Building('TH', MAX_TOWN_HALL_HEALTH, TOWN_HALL_SYMBOL)
        self.activeBuildings.append(TH)

        centerX = ROWS//2
        centerY = COLS//2
        for i in range(centerX-2, centerX+2):
            for j in range(centerY-2, centerY+1):
                self.board[i][j] = TH.symbol


    def initHut(self):
        H1 = Building('H1', MAX_HUT_HEALTH, HUT_SYMBOL)
        H2 = Building('H2', MAX_HUT_HEALTH, HUT_SYMBOL)
        H3 = Building('H3', MAX_HUT_HEALTH, HUT_SYMBOL)
        H4 = Building('H4', MAX_HUT_HEALTH, HUT_SYMBOL)
        H5 = Building('H5', MAX_HUT_HEALTH, HUT_SYMBOL)

        self.activeBuildings.append(H1)
        self.activeBuildings.append(H2)
        self.activeBuildings.append(H3)
        self.activeBuildings.append(H4)
        self.activeBuildings.append(H5)

        x1 = ROWS//4
        y1 = COLS//4
        for i in range(x1, x1+2):
            for j in range(y1-1, y1+1):
                self.board[i][j] = H1.symbol

        x2 = x1*3
        y2 = y1
        for i in range(x2, x2+2):
            for j in range(y2-1, y2+1):
                self.board[i][j] = H2.symbol

        x3 = x1
        y3 = y1*3
        for i in range(x3, x3+2):
            for j in range(y3-1, y3+1):
                self.board[i][j] = H3.symbol
        
        x4 = x1*3
        y4 = y1*3
        for i in range(x4, x4+2):
            for j in range(y4-1, y4+1):
                self.board[i][j] = H4.symbol

        x5 = x1*2
        y5 = y1
        for i in range(x5, x5+2):
            for j in range(y5-1, y5+1):
                self.board[i][j] = H5.symbol
                