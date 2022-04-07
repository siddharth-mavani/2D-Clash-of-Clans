# Importing Default Libraries
import math

# Importing Custome Modules
from defs import *
from building import Building


class Cannon(Building):
    def __init__(self, name, health, symbol, range, damage):
        super().__init__(name, health, symbol)
        self.range = range
        self.damage = damage

        self.position = []
        self.center = []
        self.target = None
        
    def addCannon(self, game, x, y):
        coord = []
        for i in range(x, x+2):
            point = [i]
            for j in range(y-1, y+1):
                point.append(j)
                coord.append(point)
                point = [i]
                game.board[i][j] = self.symbol

        self.position = coord

        avgX = 0
        avgY = 0
        for i in coord:
            avgX += i[0]
            avgY += i[1]

        avgX = avgX/len(coord)
        avgY = avgY/len(coord)

        self.center = [avgX, avgY]

    def initCannon(game):
        game.numActiveBuildings += 3

        Cannon1 = Cannon('C1', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)
        Cannon2 = Cannon('C2', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)
        Cannon3 = Cannon('C3', MAX_CANNON_HEALTH, CANNON_SYMBOL, CANNON_RANGE, CANNON_DAMAGE)

        game.activeBuildings.append(Cannon1)
        game.activeBuildings.append(Cannon2)
        game.activeBuildings.append(Cannon3)

        game.activeCannons.append(Cannon1)
        game.activeCannons.append(Cannon2)
        game.activeCannons.append(Cannon3)

        game.activeDefenseBuildings.append(Cannon1)
        game.activeDefenseBuildings.append(Cannon2)
        game.activeDefenseBuildings.append(Cannon3)

        x1 = ROWS//4
        y1 = COLS//2
        Cannon1.addCannon(game, x1, y1)

        x2 = x1*3
        y2 = y1
        Cannon2.addCannon(game, x2, y2)

        x3 = x1*2
        y3 = (COLS//4)*3
        Cannon3.addCannon(game, x3, y3)

    def getDistance(self, character):
        x1 = self.center[0]
        y1 = self.center[1]
        x2 = character.xPos
        y2 = character.yPos

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        return distance

    def getTarget(self, game):
        # Get closest barbarian or king from self
        closestTarget = None
        closestDistance = None
        activeCharacters = game.Barbarians + [game.King] + game.Archers
        for character in activeCharacters:
            distance = self.getDistance(character)
            if((closestDistance == None or distance < closestDistance) and distance <= self.range and character.isActive):
                closestTarget = character
                closestDistance = distance
        
        return closestTarget

    def attack(self, game):
        if(self.target == None):
            self.target = self.getTarget(game)

        if(self.target != None and self.target.isActive and self.getDistance(self.target) <= self.range):
            self.target.health -= self.damage

            if(self.target.health <= 0):
                if(self.target in game.Barbarians or self.target in game.Archers):
                    self.target.isActive = False
                    game.numActiveTroops -= 1
                else:
                    game.King.isActive = False
                    game.numActiveTroops -= 1

                self.target = None



def attackCannon(game):
    for cannon in game.activeCannons:
        if(cannon.isActive):
            cannon.attack(game)

