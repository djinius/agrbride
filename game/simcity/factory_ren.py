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
    upgradeBalance = [   1000,   2000,   4000,   8000,  12000,
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
        self.balance = 1000
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
            return self.getBalance() >= self.upgradeBalance[self.level]

        return False

    def getBalance(self):
        return self.balance

    def recalcStocks(self):
        pass

    def isBalanceEnough(self, amount):
        return self.balance >= amount
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount

    def upgrade(self):
        if self.isUpgradeAvailable():
            self.withdraw(self.upgradeBalance[self.level])
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
                                      "번개나무",   # localName
                                      -1,           # x
                                      -1,           # y
                                      None,         # minimapColor
                                      None,         # levelSprites
                                      [(x+1)*1000 for x in range(0, 10)],  # managements
                                      None)         # detailScreen
        self.maxlevel = 10
        self.balance = 0
        self.unlocked = False

    def unlock(self):
        self.unlocked = True

    def isUnlocked(self):
        return self.unlocked
