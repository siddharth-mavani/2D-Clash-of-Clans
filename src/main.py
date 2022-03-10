# Importing Libraries


# Importing Custom Modules
from input import input_to, Get
from defs import *
from game import Game

# Initializing Game
game = Game()

while(game.state):
    # Getting Input
    get = Get()
    key = input_to(get)
    if key == 'p':
        game.printBoard()
    elif key == 'q':
        game.state = False





