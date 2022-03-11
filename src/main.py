# Importing Libraries
import os

# Importing Custom Modules
from input import input_to, Get
from defs import *
from game import Game
from barbarian import Barbarian, spawnBarbarian

# Initializing Game
game = Game()

while(game.state):
    # Printing Board
    os.system('clear')
    game.printBoard()

    # Getting Input
    get = Get()
    key = input_to(get)

    if key == 'p':
        pass
    elif key == 'q':
        game.state = False
    elif key == '1':
        spawnBarbarian(game, 1)
    elif key == '2':
        spawnBarbarian(game, 2)
    elif key == '3':
        spawnBarbarian(game, 3)
    elif key == '4':
        for i in game.activeBuildings:
            i.health -= 26
            





