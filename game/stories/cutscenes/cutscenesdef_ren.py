"""renpy
init -1 python:
"""

################################################################################
# 컷신 클래스
# 1. 특정 조건을 만족했을 때 재생할 컷신 레이블을 담고 있음
# 2. 멤버함수
# 2.1. isAvailable(): 컷신 재생 가능
# 2.2. isFinished(): 컷신 재생 끝냄
# 2.3. getLableName(): 컷신 레이블 리턴
# 2.4. finish(): 재생 끝났음 마킹 => 컷신을 보지 않고 보상만 얻을 때 활용
# 2.5. isVerified(): 툴팁 확인 완료
# 2.6. getScreenName(): 툴팁 스크린명 - 사용 가능할 때 도시 관리 화면에 띄움
# 2.7. verify(): 툴팁 확인함 마킹
################################################################################

class CutScene:
    def __init__(self, title, labelName, screenName):
        self.finished = False
        self.verified = False
        self.title = title
        self.labelName = labelName
        self.screenName = screenName

    # 순수가상함수
    def isAvailable(self):
        raise NotImplementedError()
        return False

    def isFinished(self):
        return self.finished

    def getTitle(self):
        return self.title

    def getLabelName(self):
        return self.labelName

    def begin(self):
        global cutscenes
        cutscenes.remove(self)

    def finish(self):
        self.finished = True
        renpy.mark_label_seen(self.getLabelName())

    def isVerified(self):
        return self.verified

    def getScreenName(self):
        return self.screenName

    def verify(self):
        self.verified = False

class RosalindAppleTreeScene(CutScene):
    def __init__(self):
        super(RosalindAppleTreeScene, self).__init__("시작", "rosalindAppleTreeScene", None)

    def isAvailable(self):
        return True

    def finish(self):
        global gPopupUnlocked
        super(RosalindAppleTreeScene, self).finish()
        gPopupUnlocked = True

class RosalindResidenceScene(CutScene):
    def __init__(self):
        super(RosalindResidenceScene, self).__init__("시작", "rosalindResidenceScene", None)

    def isAvailable(self):
        return getTotalSupplyDepots() >= 1

    def finish(self):
        global gResidenceUnlocked
        super(RosalindResidenceScene, self).finish()
        gResidenceUnlocked = True

class RosalindFactoryScene(CutScene):
    def __init__(self):
        super(RosalindFactoryScene, self).__init__("공방", "rosalindFactoryScene", None)

    def isAvailable(self):
        return getTotalSupplyDepots() >= 1 and getTotalResidence() >= 1

    def finish(self):
        global gFactory

        super(RosalindFactoryScene, self).finish()
        gFactory.unlock()

class RosalindWellScene(CutScene):
    def __init__(self):
        super(RosalindWellScene, self).__init__("우물", "rosalindWellScene", None)

    def isAvailable(self):
        return (getTotalSupplyDepots() >= 4) or (getTotalWaterSupply() - getTotalWaterDemand() <= 10)

    def finish(self):
        global gWellUnlocked

        super(RosalindWellScene, self).finish()
        gWellUnlocked = True

class RosalindDateScene(CutScene):
    def __init__(self):
        super(RosalindDateScene, self).__init__("나들이", "rosalindDateScene", None)

    def isAvailable(self):
        return getAvailablePopulation() >= 1000

class RosalindUpgradeScene(CutScene):
    def __init__(self):
        super(RosalindUpgradeScene, self).__init__("등급 향상", "rosalindUpgradeScene", None)

    def isAvailable(self):
        global gFactory
        return gFactory.isWoodConsumable(500)

    def finish(self):
        super(RosalindUpgradeScene, self).finish()

class RosalindFactoryUpgradeScene(CutScene):
    def __init__(self):
        super(RosalindFactoryUpgradeScene, self).__init__("공방", "rosalindFactoryUpgradeScene", None)

    def isAvailable(self):
        global gFactory
        return (getTotalSupplyDepots() >= 5) and (getAvailablePopulation() > 2500) and (gFactory.isWoodConsumable(1000))

    def finish(self):
        global gFactory

        super(RosalindFactoryUpgradeScene, self).finish()
        gFactory.unlockUpgrade()

class MaliSharonScene(CutScene):
    def __init__(self):
        super(MaliSharonScene, self).__init__("무궁화", "maliSharonScene", None)

    def isAvailable(self):
        return getTotalSupplyDepots() >= 7

    def finish(self):
        global gSharonUnlocked

        super(MaliSharonScene, self).finish()
        gSharonUnlocked = True

def availableCutScenes(scenes):
    return [x for x in scenes if (x.isAvailable() and (not x.isFinished()))]


# 3507516605