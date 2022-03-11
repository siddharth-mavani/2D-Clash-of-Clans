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

    def move(game, direction):
        # Check if object exists in the direction
        if(direction == 'w'):
            if(game.board[game.activeKing.xPos-1][game.activeKing.yPos] != BG):
                return False
        elif(direction == 's'):
            if(game.board[game.activeKing.xPos+1][game.activeKing.yPos] != BG):
                return False
        elif(direction == 'a'):
            if(game.board[game.activeKing.xPos][game.activeKing.yPos-1] != BG):
                return False
        elif(direction == 'd'):
            if(game.board[game.activeKing.xPos][game.activeKing.yPos+1] != BG):
                return False    

        # Move the object
        if(direction == 'w'):
            game.board[game.activeKing.xPos][game.activeKing.yPos] = BG
            game.activeKing.xPos -= 1 * game.activeKing.speed
            game.activeKing.position = [[game.activeKing.xPos, game.activeKing.yPos]]
            game.board[game.activeKing.xPos][game.activeKing.yPos] = game.activeKing.symbol
        elif(direction == 's'):
            game.board[game.activeKing.xPos][game.activeKing.yPos] = BG
            game.activeKing.xPos += 1 * game.activeKing.speed
            game.activeKing.position = [[game.activeKing.xPos, game.activeKing.yPos]]
            game.board[game.activeKing.xPos][game.activeKing.yPos] = game.activeKing.symbol
        elif(direction == 'a'):
            game.board[game.activeKing.xPos][game.activeKing.yPos] = BG
            game.activeKing.yPos -= 1 * game.activeKing.speed
            game.activeKing.position = [[game.activeKing.xPos, game.activeKing.yPos]]
            game.board[game.activeKing.xPos][game.activeKing.yPos] = game.activeKing.symbol
        elif(direction == 'd'):
            game.board[game.activeKing.xPos][game.activeKing.yPos] = BG
            game.activeKing.yPos += 1 * game.activeKing.speed
            game.activeKing.position = [[game.activeKing.xPos, game.activeKing.yPos]]
            game.board[game.activeKing.xPos][game.activeKing.yPos] = game.activeKing.symbol



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