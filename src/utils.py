# Importing Custom Modules
from defs import *
from huts import Hut
from walls import Wall
from townHall import TownHall
from king import King, renderKingColor
from cannon import Cannon, attackCannon
from building import renderBuildingColor
from barbarian import renderBarbarianColor, moveBarbarians, attackBarbarians

class Game:
    def __init__(self):
        # Initializing vars
        self.board = []
        self.state = True
        self.activeBuildings = []
        self.activeCannons = []
        self.Barbarians = []
        self.King = None
        self.numActiveBuildings = 0
        self.numActiveTroops = 0
        self.result = None

        # Calling init functions
        self.initBoard()
        TownHall.initTH(self)
        Hut.initHut(self)
        King.initKing(self)
        Cannon.initCannon(self)
        Wall.initWall(self)


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
        renderKingColor(self, self.King)
        renderBarbarianColor(self, self.Barbarians)

        numHearts = int((self.King.health / MAX_KING_HEALTH) * 10)
        print("King Health: " + u'\u2665' * numHearts)

        board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end='')


    def checkGame(self):
        if(self.numActiveTroops == 0):
            self.result = 'LOSE'
            self.state = False
        elif(self.numActiveBuildings == 0):
            self.result = 'WIN'
            self.state = False

    def update(self):
        moveBarbarians(self)
        attackBarbarians(self)
        attackCannon(self)
        self.checkGame()

def saveGame(moves):
    file = open('../history/replay.txt', 'a')

    for move in moves:
        if(move == None):
            file.write("!")
        else:
            file.write(str(move))

    file.write('\n')
    file.close()