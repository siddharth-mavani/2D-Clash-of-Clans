# Import Custom Modules
from defs import *
class Building:
    def __init__(self, name, health, symbol):
        self.name = name
        self.health = health
        self.symbol = symbol

class TownHall(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)

    def renderColor():
        print("yo")

    def initTH(game):
        TH = TownHall('TH', MAX_TOWN_HALL_HEALTH, TOWN_HALL_SYMBOL)
        game.activeBuildings.append(TH)

        centerX = ROWS//2
        centerY = COLS//2
        for i in range(centerX-2, centerX+2):
            for j in range(centerY-2, centerY+1):
                game.board[i][j] = TH.symbol

class Hut(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)

    def initHut(game):
        H1 = Hut('H1', MAX_HUT_HEALTH, HUT_SYMBOL)
        H2 = Hut('H2', MAX_HUT_HEALTH, HUT_SYMBOL)
        H3 = Hut('H3', MAX_HUT_HEALTH, HUT_SYMBOL)
        H4 = Hut('H4', MAX_HUT_HEALTH, HUT_SYMBOL)
        H5 = Hut('H5', MAX_HUT_HEALTH, HUT_SYMBOL)

        game.activeBuildings.append(H1)
        game.activeBuildings.append(H2)
        game.activeBuildings.append(H3)
        game.activeBuildings.append(H4)
        game.activeBuildings.append(H5)

        x1 = ROWS//4
        y1 = COLS//4
        for i in range(x1, x1+2):
            for j in range(y1-1, y1+1):
                game.board[i][j] = H1.symbol

        x2 = x1*3
        y2 = y1
        for i in range(x2, x2+2):
            for j in range(y2-1, y2+1):
                game.board[i][j] = H2.symbol

        x3 = x1
        y3 = y1*3
        for i in range(x3, x3+2):
            for j in range(y3-1, y3+1):
                game.board[i][j] = H3.symbol
        
        x4 = x1*3
        y4 = y1*3
        for i in range(x4, x4+2):
            for j in range(y4-1, y4+1):
                game.board[i][j] = H4.symbol

        x5 = x1*2
        y5 = y1
        for i in range(x5, x5+2):
            for j in range(y5-1, y5+1):
                game.board[i][j] = H5.symbol