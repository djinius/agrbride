"""renpy
init -1 python:
"""

# 싹 -> 묘목 -> 떨기나무 -> 고목

class Building:
    def __init__(self, name, x, y, maxlevel, minimapColor, levelNames):
        global gCityMap

        self.x = x
        self.y = y
        self.name = name
        self.level = 0
        self.maxlevel = maxlevel
        self.minimapColor = minimapColor
        self.levelNames = levelNames

        gCityMap[y][x] = self

    def getIdleSprite(self):
        return "images/simcity/buildings/" + self.name + "_level" + str(self.level) + ".png"

    def isUpgradeEnabled(self):
        return self.level < self.maxlevel

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

    # 철거
    def dismantle(self):
        global gCityMap
        global gBuildings

        gCityMap[self.y][self.x] = None
        gBuildings.remove(self)

# 유실수
# 컨텍스트 메뉴: 물주기, 거름주기, 벌레잡기, 가지치기, 수확, 등급 상향, 벌목
# 등급: 싹 -> 묘목 -> 큰키나무 -> 아름드리 -> 고목
class FruitTree(Building):
    def __init__(self, name, x, y, maxlevel, minimapcolor):
        super(FruitTree, self).__init__(name, x, y, maxlevel, minimapcolor, ["싹", "묘목", "큰키나무", "아름드리", "고목"])
        self.waterFilled = 0
        self.fertilized = 0
        self.vermins = 0
        self.shaggy = 0
        self.sublevel = 1
        self.harvestAmount = 0

    def getIdleSprite(self):
        if self.level == 3:
            return "images/simcity/buildings/" + self.name + "_level" + str(self.level) + "_" + str(self.sublevel) + ".png"
        else:
            return super(FruitTree, self).getIdleSprite()

    def water(self):
        self.waterFilled += 10

    def fertilize(self):
        self.fertilized += 10

    def catchBug(self):
        self.vermins = max(self.vermins - 10, 0)

    def prune(self):
        self.shaggy = max(self.shaggy - 10, 0)

    def getContextMenu(self):
        contextMenu = {}

        if self.level in [0, 1, 2, 3]:
            contextMenu["물주기"] = (self.water, self.alwaysTrue)
            contextMenu["거름주기"] = (self.fertilize, self.alwaysTrue)
            contextMenu["벌레잡기"] = (self.catchBug, self.alwaysTrue)
            contextMenu["가지치기"] = (self.prune, self.alwaysTrue)

        if self.level == 4:
            contextMenu["수확"] = (self.harvest, self.isHarvestAvailable)

        contextMenu["벌목"] = (self.dismantle, self.alwaysTrue)
        return contextMenu

    def isHarvestAvailable(self):
        return False


class AppleTree(FruitTree):
    def __init__(self, x, y):
        super(AppleTree, self).__init__("apple", x, y, 4, "#F88")

class GrapeTree(FruitTree):
    def __init__(self, x, y):
        super(GrapeTree, self).__init__("grape", x, y, 4, "#409")

class TeaTree(FruitTree):
    def __init__(self, x, y):
        super(TeaTree, self).__init__("tea", x, y, 4, "#0F0")

    def getContextMenu(self):
        contextMenu = {}

        if self.level in [0, 1, 2, 3]:
            contextMenu["물주기"] = (self.water, self.alwaysTrue)
            contextMenu["벌레잡기"] = (self.catchBug, self.alwaysTrue)
            contextMenu["가지치기"] = (self.prune, self.alwaysTrue)

        if self.level == 4:
            contextMenu["수확"] = (self.harvest, self.isHarvestAvailable)

        contextMenu["벌목"] = (self.dismantle, self.alwaysTrue)
        return contextMenu

class RiceTree(FruitTree):
    def __init__(self, x, y):
        super(RiceTree, self).__init__("rice", x, y, 4, "#840")

class SharonTree(Building):
    def __init__(self, x, y):
        super(SharonTree, self).__init__("sharon", x, y, 3, "#FF0", ["싹", "묘목", "떨기나무"])
        self.waterFilled = 0
        self.fertilized = 0
        self.shaggy = 0

    def getContextMenu(self):
        contextMenu = {}

        contextMenu["물주기"] = (self.water, self.alwaysTrue)
        contextMenu["거름주기"] = (self.fertilize, self.alwaysTrue)
        contextMenu["가지치기"] = (self.prune, self.alwaysTrue)
        contextMenu["벌목"] = (self.dismantle, self.alwaysTrue)

        return contextMenu

class NymphaTree(Building):
    def __init__(self, x, y):
        super(NymphaTree, self).__init__("nympha", x, y, 3, "#FFF", ["싹", "연못", "호수"])

    def getContextMenu(self):
        contextMenu = {}

        contextMenu["순치기"] = (self.prune, self.alwaysTrue)
        contextMenu["뽑기"] = (self.dismantle, self.alwaysTrue)

        return contextMenu

# 증축
class Hive(Building):
    def __init__(self, x, y):
        super(Hive, self).__init__("hive", x, y, 3, "#FFF", ["숙사", "군락", "마천루"])

    def getContextMenu(self):
        contextMenu = {}

        contextMenu["철거"] = (self.dismantle, self.alwaysTrue)

        return contextMenu

