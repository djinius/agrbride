"""renpy
init -1 python:
"""

# 추가 빌딩 - 숙소

class Residence(Building):
    populations = [40, 80, 256, 768, 1920]
    levelNames = ["생활관", "숙사", "연립주택", "고층건물", "마천루"]
    levelExperience = [25, 25, 25, 25, 25]

    def __init__(self, x, y):
        super(Residence, self).__init__("residence", "주거 건물", x, y, "#44F",
                                   ["residence0", "residence1", "residence2", "residence3", "residence4"],
                                   [5, 10, 20, 50, 100])

        addExperience(25)
        if getTotalResidence() == 1:
            self.upgradeResources = [[gFactory.isWoodConsumable, gFactory.consumeWoods, 100]]

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        d = self.getDistance(x, y)
        if d == 1:
            return .3 + .15 * self.level
        else:
            return 0

    # 인구 증강 - 거주구는 증강 효과 없음
    def getPopulationBoostFactor(self, x, y):
        return 0

    def getWaterDemand(self):
        return 0

    def getContextMenu(self):
        contextMenu = {}
        contextMenu["등급 향상"] = (self.upgrade, self.isUpgradeAvailable)
        return contextMenu

    def getPopulationFactor(self):
        global gBuildings

        ret = 1.

        for b in gBuildings:
            if b != self:
                ret += b.getPopulationBoostFactor(self.x, self.y)

        return ret

    def getPopulation(self):
        return int(self.populations[self.level] * self.getPopulationFactor())

    def upgrade(self):
        super(Residence, self).upgrade()
        addExperience(15)

def getAcceptablePopulation():
    global gBuildings

    ret = 0

    for b in gBuildings:
        if isinstance(b, Residence):
            ret += b.getPopulation()

    return ret

def getTotalPopulation():
    return max(min(getAcceptablePopulation(), getTotalFoodSupply()), 8)

def getIdlePopulation():
    return max(getTotalPopulation() - getTotalManagements(), 0)
