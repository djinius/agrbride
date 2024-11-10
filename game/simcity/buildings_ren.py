"""renpy
init -1 python:
"""

# 재코딩

class Building:
    def __init__(self, name, localName, x, y, minimapColor, levelSprites, managements, detailScreen):
        global gCityMap

        self.x = x
        self.y = y
        self.name = name
        self.localName = localName
        self.level = 0
        self.minimapColor = minimapColor
        self.levelSprites = levelSprites
        self.maxlevel = len(levelSprites) - 1
        self.managements = managements
        self.detailScreen = detailScreen

        gCityMap[y][x] = self

    def getIdleSprite(self):
        return self.levelSprites[self.level]

    def isUpgradeAvailable(self):
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
        self.x = dx
        self.y = dy

    # 철거
    def dismantle(self):
        global gCityMap
        global gBuildings

        gCityMap[self.y][self.x] = None
        gBuildings.remove(self)

# 유실수
# 컨텍스트 메뉴: 물주기, 거름주기, 벌레잡기, 가지치기, 수확, 등급 상향, 벌목
# 등급: 싹 -> 묘목 -> 큰키나무 -> 아름드리 -> 고목
# 물주기, 거름주기, 가지치기를 적당히 했을 때 생명력 증가, 과하면 생명력 감소
# 벌레잡기를 꾸준히 하면 생명력 증가
# 생명력 일정수준 증가시 수확 가능
# 수확시 생명력 대폭 감소
class FruitTree(Building):
    def __init__(self, name, localName, x, y, minimapcolor, levelSprites, populations, managements, detailScreen = None):
        super(FruitTree, self).__init__(name, localName, x, y, minimapcolor, levelSprites, managements, detailScreen)
        self.populations = populations
        self.managements = managements

    def getContextMenu(self):
        contextMenu = {}
        if self.isUpgradeAvailable():
            contextMenu["등급 향상"] = (self.upgrade, self.alwaysTrue)

        return contextMenu

    def getPopulation(self):
        return self.populations[self.level] * self.getPopulationFactor()

    def getPopulationFactor(self):
        return 1.0


# 3레벨일 때에는 물주기, 비료주기, 벌레잡기, 가지치기 시 별도의 수확량 바를 증가시킴
# 동시에 서브레벨 증가
class AppleTree(FruitTree):
    def __init__(self, x, y):
        super(AppleTree, self).__init__("apple", "사과나무", x, y, "#F88", ["appleTree0", "appleTree1", "appleTree2", "appleTree3"], [100, 300, 600, 1000], [25, 75, 150, 250])
        self.population = []

class GrapeTree(FruitTree):
    def __init__(self, x, y):
        super(GrapeTree, self).__init__("grape", "포도나무", x, y, "#409", ["grapeTree0", "grapeTree1", "grapeTree2", "grapeTree3"], [200, 500, 1000, 2000])

class PeachTree(FruitTree):
    def __init__(self, x, y):
        super(PeachTree, self).__init__("peach", "포도나무", x, y, "#409", ["peachTree0", "peachTree1", "peachTree2", "peachTree3"], [200, 500, 1000, 2000])

class TeaTree(FruitTree):
    def __init__(self, x, y):
        super(TeaTree, self).__init__("tea", "차나무", x, y, "#0F0")

class SharonTree(Building):
    def __init__(self, x, y):
        super(SharonTree, self).__init__("sharon", "무궁화", x, y, "#FF0", ["roseOfSharonTree"])
        self.waterFilled = 0
        self.fertilized = 0
        self.shaggy = 0

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

