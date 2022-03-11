# Importing Custom Modules
from defs import *
from character import Character

class Barbarian(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.status = 'alive'

def spawnBarbarian(game, locID):
    if(locID == 1):
        x = 1;
        y = 1;
    elif(locID == 2):
        x = ROWS-2;
        y = 1;
    elif(locID == 3):
        x = ROWS-2;
        y = COLS-2;
    
    numBarbs = len(game.activeBarbarians)
    BarbID = 'B' + str(numBarbs+1)

    barb = Barbarian(BarbID, MAX_BARB_HEALTH, BARB_DAMAGE, BARB_SPEED, BARB_SYMBOL, x, y)
    game.activeBarbarians.append(barb)
    game.board[x][y] = barb.symbol