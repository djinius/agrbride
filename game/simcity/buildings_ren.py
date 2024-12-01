"""renpy
init -1 python:
"""

# 재코딩

class Building:
    def __init__(self, name, localName, x, y, minimapColor, levelSprites, managements, waterDemand = None, detailScreen = None):
        global gCityMap

        self.x = x
        self.y = y
        self.name = name
        self.localName = localName
        self.level = 0
        self.minimapColor = minimapColor
        self.levelSprites = levelSprites

        if levelSprites:
            self.maxlevel = len(levelSprites) - 1
        else:
            self.maxlevel = 0

        self.managements = managements
        if waterDemand is not None:
            self.waterDemand = waterDemand
        else:
            self.waterDemand = [0]

        self.detailScreen = detailScreen

        if x != -1 and y != -1:
            placeBuilding(x, y, self)
        appendBuilding(self)

    def getIdleSprite(self):
        return self.levelSprites[self.level]

    def isUpgradeAvailable(self):
        if getAvailableWater() >= self.getWaterDemand():
            return self.level < self.maxlevel
        else:
            return False

    def upgrade(self):
        if self.level < self.maxlevel:
            self.level += 1

    def getMinimapColor(self):
        return self.minimapColor

    # 컨텍스트 메뉴 - 순수가상함수
    # 리턴 자료: 딕셔너리{"메뉴 아이템", "action 함수명", "sensitive 함수명"}
    # 화면 컨텍스트 메뉴에서 메뉴 아이템을 클릭하면 함수명이 호출되는 방식
    # 서브클래스에서 만들어 줄 것
    def getContextMenu(self):
        raise NotImplementedError()

    def alwaysTrue(self):
        return True
    def alwaysFalse(self):
        return False

    # 진행바 리턴
    # 리턴 자료: 딕셔너리{"상태바 이름", "현재 수치", "최대 수치"}
    def getProgressBars(self):
        return {}

    def getContextName(self):
        return "buildingPopup"

    def getDetailScreen(self):
        return self.detailScreen

    # 관리인원
    def getManagements(self):
        return self.managements[self.level]

    # 이동
    def moveTo(self, dx, dy):
        placeBuilding(self.x, self.y, None)
        self.x = dx
        self.y = dy
        placeBuilding(self.x, self.y, self)

    # 철거
    def dismantle(self):
        placeBuilding(self.x, self.y, None)
        removeBuilding(self)

    def getWaterDemand(self):
        return self.waterDemand[self.level]

# 유실수
# 컨텍스트 메뉴: 물주기, 거름주기, 벌레잡기, 가지치기, 수확, 등급 상향, 벌목
# 등급: 싹 -> 묘목 -> 큰키나무 -> 아름드리 -> 고목
# 물주기, 거름주기, 가지치기를 적당히 했을 때 생명력 증가, 과하면 생명력 감소
# 벌레잡기를 꾸준히 하면 생명력 증가
# 생명력 일정수준 증가시 수확 가능
# 수확시 생명력 대폭 감소
class FruitTree(Building):
    def __init__(self, name, localName, x, y, minimapcolor, levelSprites, populations, managements, woods, waterDemand = None, detailScreen = None):
        super(FruitTree, self).__init__(name, localName, x, y, minimapcolor, levelSprites, managements, waterDemand, detailScreen)
        self.populations = populations
        self.managements = managements
        self.woods = woods

    def getContextMenu(self):
        contextMenu = {}
        contextMenu["등급 향상"] = (self.upgrade, self.isUpgradeAvailable)

        return contextMenu

    def getPopulation(self):
        return self.populations[self.level] * self.getPopulationFactor()

    def getPopulationFactor(self):
        return 1.0

    def getWoodProduction(self):
        return self.woods[self.level]

class AppleTree(FruitTree):
    def __init__(self, x, y):
        super(AppleTree, self).__init__("apple", "사과나무", x, y, "#F88",
                                        ["appleTree0", "appleTree1", "appleTree2", "appleTree3"],
                                        [100, 300, 600, 1000], [25, 75, 150, 250],
                                        [5, 10, 15, 20], [5, 10, 15, 20]
                                        )
        self.population = []

    def isUpgradeAvailable(self):
        global gFactory

        ret = False
        if super(AppleTree, self).isUpgradeAvailable():
            if gFactory.isWoodConsumable(500):
                ret = True

        return ret

    def upgrade(self):
        global gFactory

        if super(AppleTree, self).isUpgradeAvailable():
            gFactory.consumeWoods(500)
            super(AppleTree, self).upgrade()

class GrapeTree(FruitTree):
    def __init__(self, x, y):
        super(GrapeTree, self).__init__("grape", "포도나무", x, y, "#409",
                                        ["grapeTree0", "grapeTree1", "grapeTree2", "grapeTree3"],
                                        [200, 500, 1000, 2000], [30, 75, 150, 300],
                                        [7, 14, 21, 30], [10, 20, 30, 40])

class PeachTree(FruitTree):
    def __init__(self, x, y):
        super(PeachTree, self).__init__("peach", "포도나무", x, y, "#409",
                                        ["peachTree0", "peachTree1", "peachTree2", "peachTree3"],
                                        [500, 1000, 2000, 3500], [50, 100, 200, 350],
                                        [10, 25, 50, 75], [15, 25, 40, 55])

class TeaTree(FruitTree):
    def __init__(self, x, y):
        super(TeaTree, self).__init__("tea", "차나무", x, y, "#0F0", ["teaTree"], )

class SharonTree(Building):
    def __init__(self, x, y):
        super(SharonTree, self).__init__("sharon", "무궁화", x, y, "#FF0", ["roseOfSharonTree"])

    def getContextMenu(self):
        contextMenu = {}
        return contextMenu

class Well(Building):
    def __init__(self, x, y):
        super(Well, self).__init__("well", "우물", x, y, "#44F", ["well", "well", "well"], [5, 10, 20])

        self.waterSupply = [100, 200, 500]
        self.levelNames = ["우물", "수동 양수기", "전기 양수기"]
        self.electricDemand = [0, 0, 20]

    def getContextMenu(self):
        contextMenu = {}
        return contextMenu

def getTotalPopulation():
    global gCityMap

    ret = 0

    for lines in gCityMap:
        for b in lines:
            if isinstance(b, FruitTree):
                ret += b.getPopulation()

    return ret

def getTotalManagements():
    global gCityMap

    ret = 0

    for lines in gCityMap:
        for b in lines:
            if isinstance(b, Building):
                ret += b.getManagements()

    return ret

def getAvailablePopulation():
    return getTotalPopulation() - getTotalManagements()

def getTotalSupplyDepots():
    ret = 0

    for lines in gCityMap:
        for b in lines:
            if isinstance(b, FruitTree):
                ret += 1

    return ret
