"""renpy
init -1 python:
"""

################################################################################
# 공방 생산품
################################################################################

################################################################################
# 생산품 클래스
# 0등급 - 목재
# 1등급 - 뜨개바늘, 옷감
# 2등급 - 벽돌, 기와
# 3등급 - 

class Factory(Building):
    maxWoodStock = [  1000,   2500,   5000,  10000,  15000,
                     20000,  30000,  50000,  75000, 100000]
    upgradeWoodStock = [  1000,   2000,   4000,   8000,  12000,
                         16000,  24000,  40000,  60000,  80000]

    products = [["뜨개바늘", "옷감"], ["벽돌"]]

    def __init__(self): #, name, localName, x, y, minimapColor, levelSprites, managements, detailScreen = None):
        super(Factory, self).__init__("Factory",    # name
                                      "공방",       # localName
                                      -1,           # x
                                      -1,           # y
                                      None,         # minimapColor
                                      None,         # levelSprites
                                      [(x+1)*10 for x in range(0, 10)],  # managements
                                      None)         # detailScreen
        self.maxlevel = 10
        self.woodStock = 1000
        self.unlocked = False
        self.upgradeUnlocked = False
        self.waterDemand = [0] * 10
        self.productionQueue = []

    def unlock(self):
        self.unlocked = True

    def unlockUpgrade(self):
        self.upgradeUnlocked = True

    def isUnlocked(self):
        return self.unlocked

    def isUpgradeAvailable(self):
        if self.upgradeUnlocked and super(Factory, self).isUpgradeAvailable():
            return self.getWoodStock() >= self.upgradeWoodStock[self.level]

        return False

    def getWoodStock(self):
        return self.woodStock

    def recalcStocks(self):
        global gBuildings

        newWoodStock = self.woodStock

        for b in gBuildings:
            if isinstance(b, FruitTree):
                newWoodStock += b.getWoodProduction()

        self.woodStock = min(newWoodStock, self.maxWoodStock[self.level])

    def isWoodConsumable(self, amount):
        return self.woodStock >= amount
        
    def consumeWoods(self, amount):
        self.woodStock -= amount

    def getMaxWoodStock(self):
        return self.maxWoodStock[self.level]

    def upgrade(self):
        if self.isUpgradeAvailable():
            self.consumeWoods(self.upgradeWoodStock[self.level])
            super(Factory, self).upgrade()

    # 관리인원
    def getManagements(self):
        if self.isUnlocked():
            return self.managements[self.level]
        else:
            return 0


class PowerPlant(Building):
    def __init__(self): #, name, localName, x, y, minimapColor, levelSprites, managements, detailScreen = None):
        super(Factory, self).__init__("PowerPlant", # name
                                      "전기나무",   # localName
                                      -1,           # x
                                      -1,           # y
                                      None,         # minimapColor
                                      None,         # levelSprites
                                      [(x+1)*1000 for x in range(0, 10)],  # managements
                                      None)         # detailScreen
        self.maxlevel = 10
        self.woodStock = 0
        self.unlocked = False

    def unlock(self):
        self.unlocked = True

    def isUnlocked(self):
        return self.unlocked
