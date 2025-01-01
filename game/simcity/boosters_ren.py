"""renpy
init -1 python:
"""

import math

# 인구, 식량 증강 건물들
# 무궁화나무
# 우물
# 체육관
# 차원문 정류장
# 텃밭

# 무궁화나무
class SharonTree(Building):
    foodBoosts = [.3, .5, .7]
    popBoost = [.1, .15, .2]

    def __init__(self, x, y):
        super(SharonTree, self).__init__("sharon", "무궁화", x, y, "#FF0",
                                         ["roseOfSharonTree"],
                                         [125], [30])

    def getContextMenu(self):
        contextMenu = {}
        return contextMenu

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        d = self.getDistance(x, y)
        ret = self.foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25
        else:
            ret = 0

        return ret

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):

        return 0

# 우물
class Well(Building):
    foodBoosts = [1., 1.5, 2., 3.]
    popBoost = [.5, .75, 1., 1.5]

    def __init__(self, x, y):
        super(Well, self).__init__("well", "우물", x, y, "#44F", ["well0", "well1", "well2", "well3"], [5, 10, 20, 35])

        self.waterSupply = [100, 200, 500, 1000]
        self.levelNames = ["우물", "수동 두레박", "도르래 두레박", "분수"]

    def getWaterDemand(self):
        return 0

    def getWaterSupply(self):
        return self.waterSupply[self.level]

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        d = self.getDistance(x, y)
        ret = self.foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25
        elif d <= 9:
            ret *= .1
        else:
            ret = 0

        return ret

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):

        d = self.getDistance(x, y)
        ret = self.foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25
        elif d <= 4:
            ret *= .1
        else:
            ret = 0

        return ret

# 체육관
class Gym(Building):
    foodBoosts = [.15, .2, .25]
    popBoost = [.2, .25, .3]

    def __init__(self, x, y):
        super(Gym, self).__init__("gym", "운동장", x, y, "#FFF", ["gym"], [15], [5], None)

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        return 0

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):

        d = self.getDistance(x, y)
        ret = self.foodBoosts[self.level]

        if d <= 1:
            pass
        elif d <= 2:
            ret *= .5
        elif d <= 4:
            ret *= .25
        else:
            ret = 0

        return ret

# 텃밭
class Garden(Building):
    popBoost = [.75, 1., 1.5]

    def __init__(self, x, y):
        super(Garden, self).__init__("garden", "텃밭", x, y, "#FFF", ["gym"], [15], [5], None)

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        d = self.getDistance(x, y)

        if d <= 1:
            ret = .15
        else:
            ret = 0

        return ret

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):
        d = self.getDistance(x, y)
        ret = self.foodBoosts[self.level]

        if d <= 1:
            ret = .75
        else:
            ret = 0
            
        return ret

# 차원문 정류장
class PortalStop(Building):
    foodBoosts = [1.5]
    popBoost = [3.]

    def __init__(self, x, y):
        super(PortalStop, self).__init__("portal", "차원문 정류장", x, y, "#FFF", ["portal"], [15], [0], None)

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        d = self.getDistance(x, y)

        if d <= 1:
            return 1.5
        else:
            return 0

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):
        d = self.getDistance(x, y)

        if d <= 1:
            return 3.
        else:
            return 0
