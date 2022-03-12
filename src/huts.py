# Importing Custome Modules
from defs import *
from building import Building


class Hut(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)
        self.position = []
        self.center = []

    def addHut(self, game, x, y):
        coord = []
        for i in range(x, x+2):
            point = [i]
            for j in range(y-1, y+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = self.symbol

        self.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        self.center = [avgX, avgY]

    def initHut(game):
        game.numActiveBuildings += 5
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
        H1.addHut(game, x1, y1)


        x2 = x1*3
        y2 = y1
        H2.addHut(game, x2, y2)

        x3 = x1
        y3 = y1*3
        H3.addHut(game, x3, y3)
        
        x4 = x1*3
        y4 = y1*3
        H4.addHut(game, x4, y4)

        x5 = x1*2
        y5 = y1
        H5.addHut(game, x5, y5)

