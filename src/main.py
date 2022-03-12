# Importing Libraries
import os

# Importing Custom Modules
from input import input_to, Get
from defs import *
from game import Game
from barbarian import spawnBarbarian
from king import King, attackKing

# Initializing Game
game = Game()

while(game.state):
    # Printing Board
    os.system('clear')
    game.printBoard()

    # Getting Input
    get = Get()
    key = input_to(get)

    # Handling Input
    if key == 'p':
        pass
    elif key == 'q':
        game.state = False
    elif key in ['1', '2', '3']:
        spawnBarbarian(game, int(key))
    elif key in ['w', 'a', 's', 'd']:
        King.move(game,key)
    elif key == '4':
        for i in game.activeBuildings:
            i.health -= 26
    elif key == ' ':
        attackKing(game)
        
    game.update()


os.system('clear')
if(game.result == 'WIN'):
    print('YOU WIN :)')
elif(game.result == 'LOSE'):
    print('YOU LOSE :(')