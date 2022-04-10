# Importing Default Libraries
from colorama import Back, Style

# Importing Custom Modules
from defs import *
from character import Character

class Queen(Character):
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        super().__init__(name, health, damage, speed, symbol, xPos, yPos)
        self.position = [[xPos, yPos]]

    def initQueen(game):
        queen = Queen('queen', MAX_QUEEN_HEALTH, QUEEN_DAMAGE, QUEEN_SPEED, QUEEN_SYMBOL, 1, COLS-2)
        game.board[queen.xPos][queen.yPos] = queen.symbol
        game.MC = queen

    def move(game, direction):
        # Check if object exists in the direction
        if(direction == 'w'):
            if(game.board[game.MC.xPos-2][game.MC.yPos] != BG):
                return False
        elif(direction == 's'):
            if(game.board[game.MC.xPos+2][game.MC.yPos] != BG):
                return False
        elif(direction == 'a'):
            if(game.board[game.MC.xPos][game.MC.yPos-2] != BG):
                return False
        elif(direction == 'd'):
            if(game.board[game.MC.xPos][game.MC.yPos+2] != BG):
                return False    

        # Move the object
        if(direction == 'w'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.xPos -= 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 's'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.xPos += 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 'a'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.yPos -= 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol
        elif(direction == 'd'):
            game.board[game.MC.xPos][game.MC.yPos] = BG
            game.MC.yPos += 1 * game.MC.speed
            game.MC.position = [[game.MC.xPos, game.MC.yPos]]
            game.board[game.MC.xPos][game.MC.yPos] = game.MC.symbol


    def attack(self, game, direction):
        print("Queen Attack Here:" + direction)


def renderQueenColor(game, queen):

    if(game.MC == None):
        return

    if queen.health <= 0:
        queen.symbol = BG
        for i in queen.position:
            game.board[i[0]][i[1]] = BG
    elif(queen.health <= 0.25 * MAX_QUEEN_HEALTH):
        queen.symbol = Back.RED + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol
    elif(queen.health <= 0.75 * MAX_QUEEN_HEALTH):
        queen.symbol = Back.YELLOW + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol
    else:
        queen.symbol = Back.GREEN + QUEEN_SYMBOL + Style.RESET_ALL
        for i in queen.position:
            game.board[i[0]][i[1]] = queen.symbol


def attackQueen(game, direction):
    queen = game.MC
    queen.attack(game, direction)