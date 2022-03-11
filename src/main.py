# Importing Libraries
import os

# Importing Custom Modules
from input import input_to, Get
from defs import *
from game import Game

# Initializing Game
game = Game()

while(game.state):
    # Printing Board
    

    # Getting Input
    get = Get()
    key = input_to(get)

    if key == 'p':
        os.system('clear')
        game.printBoard()
    elif key == 'q':
        game.state = False





