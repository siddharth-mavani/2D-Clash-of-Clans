# Importing Default Libraries
from colorama import Back, Style

# Import Custom Modules
from defs import *

class Building:
    def __init__(self, name, health, symbol):
        self.name = name
        self.health = health
        self.symbol = symbol




def renderBuildingColor(game, activeBuildings):
    renderColorTH(game, activeBuildings[0])
    renderColorHut(game, activeBuildings[1:6])
    renderColorCannon(game, activeBuildings[6:])

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
        TH.symbol = Back.RED + TOWN_HALL_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    elif(TH.health <= 0.75 * MAX_TOWN_HALL_HEALTH):
        TH.symbol = Back.YELLOW + TOWN_HALL_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    else:
        TH.symbol = Back.GREEN + TOWN_HALL_SYMBOL + Style.RESET_ALL
        for i in TH.position:
            game.board[i[0]][i[1]] = TH.symbol
    
def renderColorCannon(game, cannons):
    for cannon in cannons:
        if cannon.health <= 0:
            cannon.symbol = BG
            for i in cannon.position:
                game.board[i[0]][i[1]] = BG
        elif(cannon.health <= 0.25 * MAX_CANNON_HEALTH):
            cannon.symbol = Back.RED + CANNON_SYMBOL + Style.RESET_ALL
            for i in cannon.position:
                game.board[i[0]][i[1]] = cannon.symbol
        elif(cannon.health <= 0.75 * MAX_CANNON_HEALTH):
            cannon.symbol = Back.YELLOW + CANNON_SYMBOL + Style.RESET_ALL
            for i in cannon.position:
                game.board[i[0]][i[1]] = cannon.symbol
        else:
            cannon.symbol = Back.GREEN + CANNON_SYMBOL + Style.RESET_ALL
            for i in cannon.position:
                game.board[i[0]][i[1]] = cannon.symbol