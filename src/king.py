# Importing Custom Modules
from defs import *
from character import Character

class King(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.status = 'alive'

    def initKing(game):
        king = King('King', MAX_KING_HEALTH, KING_DAMAGE, KING_SPEED, KING_SYMBOL, 1, COLS-2)
        game.board[king.xPos][king.yPos] = king.symbol