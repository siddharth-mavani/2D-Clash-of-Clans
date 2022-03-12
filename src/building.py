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
    