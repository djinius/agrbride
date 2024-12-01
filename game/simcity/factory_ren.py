"""renpy
init -1 python:
"""

################################################################################
# 공방 생산품
################################################################################

################################################################################
# 생산품 클래스
# 목재 - 영지 등급 0

class Factory(Building):
    maxWoodStock = [  1000,   2500,   5000,  10000,  15000,
                     20000,  30000,  50000,  75000, 100000]

    def __init__(self): #, name, localName, x, y, minimapColor, levelSprites, managements, detailScreen = None):
        super(Factory, self).__init__("Factory",    # name
                                      "공방",       # localName
                                      -1,           # x
                                      -1,           # y
                                      None,         # minimapColor
                                      None,         # levelSprites
                                      [(x+1)*500 for x in range(0, 10)],  # managements
                                      None)         # detailScreen
        self.maxlevel = 10
        self.woodStock = 0
        self.unlocked = False
        self.upgradeUnlocked = False

    def unlock(self):
        self.unlocked = True

    def unlockUpgrade(self):
        self.upgradeUnlocked = True

    def isUnlocked(self):
        return self.unlocked

    def getWoodStock(self):
        return self.woodStock

    def recalcStocks(self):
        global gBuildings

        newWoodStock = 0

        for b in gBuildings:
            if isinstance(b, FruitTree):
                print(b.name, b.getWoodProduction())
                newWoodStock += b.getWoodProduction()

        self.woodStock = min(self.woodStock + newWoodStock, self.maxWoodStock[self.level])

    def isWoodConsumable(self, amount):
        return self.woodStock >= amount
        
    def consumeWoods(self, amount):
        self.woodStock -= amount

    def getMaxWoodStock(self):
        return self.maxWoodStock[self.level - 1]

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
