# Importing Custom Modules
from defs import *

class rageSpell:
    def __init__(self):
        pass

    def cast(self, game):
        # double speed and damage of all active barbarians
        for i in game.activeBarbarians:
            if(i.isActive):
                i.speed *= 2
                i.damage *= 2
        
        if(game.activeKing.isActive):
            game.activeKing.speed *= 2
            game.activeKing.damage *= 2

class healSpell:
    def __init__(self):
        pass

    def cast(self, game):
        # 1.5 times health of all barbarians
        for i in game.activeBarbarians:
            if(i.isActive):
                if(i.health * 1.5 >= MAX_BARB_HEALTH):
                    i.health = MAX_BARB_HEALTH
                else:
                    i.health *= 1.5

        if(game.activeKing.isActive):
            if(game.activeKing.health * 1.5 >= MAX_KING_HEALTH):
                game.activeKing.health = MAX_KING_HEALTH
            else:
                game.activeKing.health *= 1.5



def castSpell(game, type):
    if(type == 'r'):
        rageSpell().cast(game)
    elif(type == 'h'):
        healSpell().cast(game)