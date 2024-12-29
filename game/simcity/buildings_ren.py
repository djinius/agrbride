"""renpy
init -2 python:
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
        self.upgradeResources = None
        self.upgradeInterval = renpy.random.randint(5, 10)

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
        if (self.level < self.maxlevel) and (self.upgradeResources is not None):
            ret = True

            for f, c, r in self.upgradeResources:
                if not f(r):
                    ret = False
                    break
        
            return ret

        else:
            return False

    def upgrade(self):
        if self.level < self.maxlevel:
            for f, c, r in self.upgradeResources:
                c(r)

            self.level += 1
            self.upgradeResources = None
            self.upgradeInterval = renpy.random.randint(5, 10)

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

    # 업그레이드 리소스 결정
    # 형식: 리스트 - f, c, r
    ## f: True/False 리턴, r 소모 가능 여부
    ## c: r 소모
    ## r: 업그레이드 필요 자원
    def chooseUpgradeResource(self):
        global gFactory
        
        if self.level < self.maxlevel:
            if self.upgradeInterval > 0:
                self.upgradeInterval -= 1
            elif self.upgradeResources is None:
                # 목재 100은 기본으로 깔고 간다
                self.upgradeResources = [[gFactory.isWoodConsumable, gFactory.consumeWoods, 100]]

                # 여타 자원 등 결정

    # 건물의 식량, 인구 증강 팩터
    def getDistance(self, x, y):
        dx = self.x - x
        dy = self.y - y
        d = (dx * dx) + (dy * dy)
        return d

    # 식량 생산 증강
    def getProductionBoostFactor(self, x, y):
        return 0

    # 인구 증강
    def getPopulationBoostFactor(self, x, y):
        return 0

    def getProductionFactor(self):
        global gBuildings

        ret = 1.

        for b in gBuildings:
            if b != self:
                ret += b.getProductionBoostFactor(self.x, self.y)

        return ret

def getTotalManagements():
    global gCityMap

    ret = 0

    for b in gBuildings:
        if isinstance(b, Building):
            ret += b.getManagements()

    return ret

def getTotalResidence():
    ret = 0

    for b in gBuildings:
        if isinstance(b, Residence):
            ret += 1

    return ret

def manageBuildings():
    global gFactory
    global gBuildings

    for b in gBuildings:
        b.chooseUpgradeResource()

    if gFactory.isUnlocked():
        gFactory.recalcStocks()