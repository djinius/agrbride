"""renpy
init -1 python:
"""

# 추가 빌딩 - 숙소

class Residence(Building):
    populations = [40, 80, 256, 768, 1920]
    levelNames = ["생활관", "숙사", "연립주택", "고층건물", "마천루"]

    def __init__(self, x, y):
        super(Residence, self).__init__("residence", "주거 건물", x, y, "#44F",
                                   ["residence0", "residence1", "residence2", "residence3", "residence4"],
                                   [5, 10, 20, 50, 100])

    def getBoostFactor(self):
        return .3 + .15 * self.level

    def getWaterDemand(self):
        return 0

    def getContextMenu(self):
        contextMenu = {}
        contextMenu["등급 향상"] = (self.upgrade, self.isUpgradeAvailable)
        return contextMenu

    def getPopulationFactor(self):
        return 1.0

    def getPopulation(self):
        return int(self.populations[self.level] * self.getPopulationFactor())

    def isUpgradeAvailable(self):
        global gFactory

        ret = False
        if super(Residence, self).isUpgradeAvailable():
            if gFactory.isWoodConsumable(500):
                ret = True

        return ret

    def upgrade(self):
        global gFactory

        if super(Residence, self).isUpgradeAvailable():
            gFactory.consumeWoods(500)
            super(Residence, self).upgrade()

def getTotalPopulation():
    global gBuildings

    ret = 8
    for b in gBuildings:
        if isinstance(b, Residence):
            ret += b.getPopulation()

    return ret

def getAvailablePopulation():
    return getTotalPopulation() - getTotalManagements()
