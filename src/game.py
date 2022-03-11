# Importing Custom Modules
from defs import *
from building import TownHall, Hut, renderBuildingColor
from king import King, renderKingColor
from barbarian import renderBarbarianColor

class Game:
    def __init__(self):
        # Initializing vars
        self.board = []
        self.state = True
        self.activeBuildings = []
        self.activeBarbarians = []
        self.activeKing = None
        self.numActiveBuildings = 0

        # Calling init functions
        self.initBoard()
        TownHall.initTH(self)
        Hut.initHut(self)
        King.initKing(self)


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
                    row.append(TOP_WALL)
                elif(j == 0 or j == COLS-1):
                    row.append(SIDE_WALL)
                else:
                    row.append(BG)
            row.append('\n')
            self.board.append(row)
    
    def printBoard(self):

        renderBuildingColor(self, self.activeBuildings)
        renderKingColor(self, self.activeKing)
        renderBarbarianColor(self, self.activeBarbarians)

        board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end='')