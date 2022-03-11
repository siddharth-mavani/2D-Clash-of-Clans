# Importing Default Libraries
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character

class King(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.status = 'alive'
        self.position = [[xPos, yPos]]

    def initKing(game):
        king = King('King', MAX_KING_HEALTH, KING_DAMAGE, KING_SPEED, KING_SYMBOL, 1, COLS-2)
        game.board[king.xPos][king.yPos] = king.symbol
        game.activeKing = king


def renderKingColor(game, king):
    if king.health <= 0:
        king.symbol = BG
        for i in king.position:
            game.board[i[0]][i[1]] = BG
    elif(king.health <= 0.25 * MAX_KING_HEALTH):
        king.symbol = Back.RED + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol
    elif(king.health <= 0.75 * MAX_KING_HEALTH):
        king.symbol = Back.YELLOW + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol
    else:
        king.symbol = Back.GREEN + KING_SYMBOL + Style.RESET_ALL
        for i in king.position:
            game.board[i[0]][i[1]] = king.symbol