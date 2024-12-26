"""renpy
init -1 python:
"""

# 유실수
# 컨텍스트 메뉴: 물주기, 거름주기, 벌레잡기, 가지치기, 수확, 등급 상향, 벌목
# 등급: 싹 -> 묘목 -> 큰키나무 -> 아름드리 -> 고목
# 물주기, 거름주기, 가지치기를 적당히 했을 때 생명력 증가, 과하면 생명력 감소
# 벌레잡기를 꾸준히 하면 생명력 증가
# 생명력 일정수준 증가시 수확 가능
# 수확시 생명력 대폭 감소
class FruitTree(Building):
    def __init__(self, name, localName, x, y, minimapcolor, levelSprites, foodSupply, managements, woods, waterDemand = None, detailScreen = None):
        super(FruitTree, self).__init__(name, localName, x, y, minimapcolor, levelSprites, managements, waterDemand, detailScreen)
        self.foodSupply = foodSupply
        self.managements = managements
        self.woods = woods

    def getContextMenu(self):
        contextMenu = {}

        if self.level < self.maxlevel:
            contextMenu["등급 향상"] = (self.upgrade, self.isUpgradeAvailable)

        return contextMenu

    def getFoodSupply(self):
        return int(self.foodSupply[self.level] * self.getFoodSupplyFactor())

    def getFoodSupplyFactor(self):
        global gCityMap
        x = self.x
        y = self.y
        factor = 1.

        for sy in [y - 1, y, y + 1]:
            for sx in [x - 1, x, x + 1]:
                if sx >= 0 and sx < 20 and sy >= 0 and sy < 16:
                    b = getBuilding(sx, sy)
                    if isinstance(b, Residence):
                        factor += b.getFoodSupplyBoostFactor()

        return factor

    def getWoodProduction(self):
        return int(self.woods[self.level] * self.getFoodSupplyFactor())

class AppleTree(FruitTree):
    def __init__(self, x, y):
        global gAppleTrees

        super(AppleTree, self).__init__("apple", "사과나무", x, y, "#F88",
                                        ["appleTree0", "appleTree1", "appleTree2", "appleTree3"],
                                        [50, 150, 250, 400], [25, 75, 150, 250],
                                        [10, 15, 25, 50], [5, 10, 15, 20]
                                        )
        gAppleTrees += 1
        addExperience(25)

    def upgrade(self):
        super(AppleTree, self).upgrade()
        addExperience(15)

class GrapeTree(FruitTree):
    def __init__(self, x, y):
        global gGrapeTrees

        super(GrapeTree, self).__init__("grape", "포도나무", x, y, "#409",
                                        ["grapeTree0", "grapeTree1", "grapeTree2", "grapeTree3"],
                                        [200, 500, 1000, 2000], [30, 75, 150, 300],
                                        [7, 14, 21, 30], [10, 20, 30, 40])

        gGrapeTrees += 1
        addExperience(50)

class PeachTree(FruitTree):
    def __init__(self, x, y):
        global gPeachTrees

        super(PeachTree, self).__init__("peach", "포도나무", x, y, "#409",
                                        ["peachTree0", "peachTree1", "peachTree2", "peachTree3"],
                                        [500, 1000, 2000, 3500], [50, 100, 200, 350],
                                        [10, 25, 50, 75], [15, 25, 40, 55])

        gPeachTrees += 1
        addExperience(75)

class TeaTree(FruitTree):
    def __init__(self, x, y):
        super(TeaTree, self).__init__("tea", "차나무", x, y, "#0F0", ["teaTree"], )

def getTotalFoodSupply():
    global gCityMap

    ret = 0

    for b in gBuildings:
        if isinstance(b, FruitTree):
            ret += b.getFoodSupply()

    return ret

def getTotalAppleTrees():
    global gAppleTrees
    return gAppleTrees

