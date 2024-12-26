"""renpy
init -1 python:
"""

import math

# 인구, 식량 증강 건물들

class Booster(Building):
    def __init__(self, name, localName, x, y, minimapColor, levelSprites, managements, waterDemand = None, detailScreen = None):
        super(Booster, self).__init__(name, localName, x, y, minimapColor, levelSprites, managements, waterDemand, detailScreen)

    def getDistance(self, x, y):
        dx = self.x - x
        dy = self.y - y
        d = (dx * dx) + (dy * dy)
        return d

    # 식량 생산 증강
    def getFoodSupplyBoostFactor(self, x, y):
        raise NotImplementedError()

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):
        raise NotImplementedError()

# 체육관

class Gym(Booster):
    def __init__(self, x, y):
        super(Booster, self).__init__("gym", "운동장", x, y, "#FFF", ["gym"], [15], [5], None)

        self.foodBoosts = [.15, .2, .25]
        self.popBoost = [.2, .25, .3]

    # 식량 생산 증강
    def getFoodSupplyBoostFactor(self, x, y):
        d = self.getDistance(x, y)
        ret = foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25

        return ret

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):

        d = self.getDistance(x, y)
        ret = foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25

        return ret

