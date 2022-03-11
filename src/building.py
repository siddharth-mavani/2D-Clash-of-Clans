# Importing Default Libraries
from colorama import Back, Style

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
        self.position = []
        self.center = []

    def initTH(game):
        TH = TownHall('TH', MAX_TOWN_HALL_HEALTH, TOWN_HALL_SYMBOL)
        game.activeBuildings.append(TH)

        centerX = ROWS//2
        centerY = COLS//2
        coord = []
        for i in range(centerX-2, centerX+2):
            point = [i]
            for j in range(centerY-2, centerY+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = TH.symbol
            
        TH.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        TH.center = [avgX, avgY]

class Hut(Building):
    def __init__(self, name, health, symbol):
        super().__init__(name, health, symbol)
        self.position = []
        self.center = []

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


def renderBuildingColor(game, activeBuildings):
    renderColorHut(game, activeBuildings[1:])
    renderColorTH(game, activeBuildings[0])


def renderColorHut(game, huts):
    for hut in huts:
        if hut.health <= 0:
            hut.symbol = BG
            for i in hut.position:
                game.board[i[0]][i[1]] = BG
        elif(hut.health <= 0.25 * MAX_HUT_HEALTH):
            hut.symbol = Back.RED + HUT_SYMBOL + Style.RESET_ALL
            for i in hut.position:
                game.board[i[0]][i[1]] = hut.symbol
        elif(hut.health <= 0.75 * MAX_HUT_HEALTH):
            hut.symbol = Back.YELLOW + HUT_SYMBOL + Style.RESET_ALL
            for i in hut.position:
                game.board[i[0]][i[1]] = hut.symbol
        else:
            hut.symbol = Back.GREEN + HUT_SYMBOL + Style.RESET_ALL
            for i in hut.position:
                game.board[i[0]][i[1]] = hut.symbol

def renderColorTH(game, TH):
    if TH.health <= 0:
        TH.symbol = BG
        for i in TH.position:
            game.board[i[0]][i[1]] = BG
    elif(TH.health <= 0.25 * MAX_TOWN_HALL_HEALTH):
        TH.symbol = Back.RED + HUT_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    elif(TH.health <= 0.75 * MAX_TOWN_HALL_HEALTH):
        TH.symbol = Back.YELLOW + HUT_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    else:
        TH.symbol = Back.GREEN + HUT_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    