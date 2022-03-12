# Importing Custome Modules
from defs import *
from building import Building


class Hut(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)
        self.position = []
        self.center = []

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
        coord = []
        for i in range(x1, x1+2):
            point = [i]
            for j in range(y1-1, y1+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = H1.symbol

        H1.position = coord
       
        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]
        avgX = avgX/len(coord)
        avgY = avgY/len(coord)
        H1.center = [avgX, avgY]


        x2 = x1*3
        y2 = y1
        coord = []
        for i in range(x2, x2+2):
            point = [i]
            for j in range(y2-1, y2+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = H2.symbol

        H2.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]
        avgX = avgX/len(coord)
        avgY = avgY/len(coord)
        H2.center = [avgX, avgY]

        x3 = x1
        y3 = y1*3
        coord = []
        for i in range(x3, x3+2):
            point = [i]
            for j in range(y3-1, y3+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = H3.symbol

        H3.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]
        avgX = avgX/len(coord)
        avgY = avgY/len(coord)
        H3.center = [avgX, avgY]
        
        x4 = x1*3
        y4 = y1*3
        coord = []
        for i in range(x4, x4+2):
            point = [i]
            for j in range(y4-1, y4+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = H4.symbol

        H4.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]
        avgX = avgX/len(coord)
        avgY = avgY/len(coord)
        H4.center = [avgX, avgY]

        x5 = x1*2
        y5 = y1
        coord = []
        for i in range(x5, x5+2):
            point = [i]
            for j in range(y5-1, y5+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = H5.symbol

        H5.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]
        avgX = avgX/len(coord)
        avgY = avgY/len(coord)
        H5.center = [avgX, avgY]
