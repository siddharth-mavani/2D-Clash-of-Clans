# Importing Libraries
import os

# Importing Custom Modules
from input import input_to, Get
from defs import *
from utils import Game, saveGame, spawnCharacter
from spells import castSpell
from king import King, attackKing

# Initializing Game

moves = []

for level in [1, 2, 3]:
    game = Game(level, MAX_BARBARIANS, MAX_ARCHERS, MAX_BALLOONS)

    while(game.state):
        # Printing Board
        os.system('clear')
        game.printBoard()

        # Getting Input
        get = Get()
        key = input_to(get)
        moves.append(key)

        # Handling Input
        if key == 'q':
            game.state = False
        elif key in ['1', '2', '3']:
            spawnCharacter(game, int(key))
        elif key in ['w', 'a', 's', 'd']:
            King.move(game,key)
        elif key in ['r', 'h']:
            castSpell(game, key)
        elif key == ' ':
            attackKing(game)
        elif key == 'b':
            game.currChar = "Barbarian"
        elif key == 'n':
            game.currChar = "Archer"
        elif key == 'm':
            game.currChar = "Balloon"
        
        game.update()

    print("LEVEL UP!")
    MAX_BARBARIANS += 2
    MAX_ARCHERS += 2
    MAX_BALLOONS += 1


saveGame(moves)

os.system('clear')
print('YOU WIN :)')