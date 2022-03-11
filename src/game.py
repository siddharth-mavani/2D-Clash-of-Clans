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

    def initBoard(self):
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                row.append(BG)
            row.append('\n')
            self.board.append(row)
    
    def printBoard(self):
        board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end='')

    def initTH(self):
        TH = Building('TH', TOWN_HALL_HEALTH, TOWN_HALL_SYMBOL)
        self.activeBuildings.append(TH)

        centerX = ROWS//2
        centerY = COLS//2
        for i in range(centerX-2, centerX+2):
            for j in range(centerY-2, centerY+1):
                self.board[i][j] = TH.symbol

    





