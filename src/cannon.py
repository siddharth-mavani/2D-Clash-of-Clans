# Importing Custome Modules
from defs import *
from building import Building


class Cannon(Building):
    def __init__(self, name, health, symbol, range, damage):
        super().__init__(name, health, symbol)
        self.range = range
        self.damage = damage

        self.position = []
        self.center = []
        

    def initCannon(game):
        game.numActiveBuildings += 3

        Cannon1 = Cannon('C1', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)
        Cannon2 = Cannon('C2', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)
        Cannon3 = Cannon('C3', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)

        game.activeBuildings.append(Cannon1)
        game.activeBuildings.append(Cannon2)
        game.activeBuildings.append(Cannon3)

        x1 = ROWS//4
        y1 = COLS//2
        coord = []
        for i in range(x1, x1+2):
            point = [i]
            for j in range(y1-1, y1+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = Cannon1.symbol

        Cannon1.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        Cannon1.center = [avgX, avgY]


        x2 = x1*3
        y2 = y1
        coord = []
        for i in range(x2, x2+2):
            point = [i]
            for j in range(y2-1, y2+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = Cannon2.symbol

        Cannon2.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        Cannon2.center = [avgX, avgY]

        x3 = x1*2
        y3 = (COLS//4)*3
        coord = []
        for i in range(x3, x3+2):
            point = [i]
            for j in range(y3-1, y3+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = Cannon3.symbol

        Cannon3.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        Cannon3.center = [avgX, avgY]


