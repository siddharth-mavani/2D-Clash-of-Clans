# Importing Default Libraries
import math

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
        self.isActive = True

    def getDistance(self, building):
        return math.sqrt((self.xPos - building.center[0])**2 + (self.yPos - building.center[1])**2)

    def getClosestBuilding(self, game):
        # Get the closest building from self
        closestBuilding = None
        closestDistance = None
        for building in game.activeBuildings:
            distance = self.getDistance(building)
            if(closestDistance == None or distance < closestDistance):
                closestBuilding = building
                closestDistance = distance
        
        return closestBuilding

    def attack(self, game):

        # Get the closest building from self
        closestBuilding = self.getClosestBuilding(game)

        checkSides = [self.xPos+1, self.yPos] in closestBuilding.position or [self.xPos-1, self.yPos] in closestBuilding.position or [self.xPos, self.yPos+1] in closestBuilding.position or [self.xPos, self.yPos-1] in closestBuilding.position
        checkCorners = [self.xPos+1, self.yPos+1] in closestBuilding.position or [self.xPos+1, self.yPos-1] in closestBuilding.position or [self.xPos-1, self.yPos+1] in closestBuilding.position or [self.xPos-1, self.yPos-1] in closestBuilding.position

        # Check if barbarians next move is coinciding with building.symbol
        if(checkSides or checkCorners):
            # Attack building
            closestBuilding.health -= self.damage

            if(closestBuilding.health <= 0):
                # make position of building equal to BG

                for i in closestBuilding.position:
                    game.board[i[0]][i[1]] = BG

                # set center of building to 
                closestBuilding.center = [100000, 100000]
                game.numActiveBuildings -= 1

