# Importing Custom Modules
from defs import *

class Character:
    def __init__(self, name, health, damage, speed, symbol, xPos, yPos):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.symbol = symbol
        self.xPos = xPos
        self.yPos = yPos
        self.status = 'alive'

    