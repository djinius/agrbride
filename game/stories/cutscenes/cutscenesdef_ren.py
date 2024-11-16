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
# 2.4. finish(): 재생 끝났음 마킹
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

    def finish(self):
        global cutscenes
        self.finished = True
        cutscenes.remove(self)

    def isVerified(self):
        return self.verified

    def getScreenName(self):
        return self.screenName

    def verify(self):
        self.verified = False

class RosalindBedScene(CutScene):
    def __init__(self):
        super(RosalindBedScene, self).__init__("첫날밤", "rosalind_bedscene", None)

    def isAvailable(self):
        return getAvailablePopulation() >= 1000


class SunnaWellScene(CutScene):
    def __init__(self):
        super(SunnaWellScene, self).__init__("우물", "sunnaWellScene", None)

    def isAvailable(self):
        return getTotalSupplyDepots() >= 2

    def finish(self):
        global gWellUnlocked

        super(SunnaWellScene, self).finish()
        gWellUnlocked = True


class MaliSharonScene(CutScene):
    def __init__(self):
        super(MaliSharonScene, self).__init__("무궁화", "maliSharonScene", None)

    def isAvailable(self):
        return getTotalSupplyDepots() >= 5


def availableCutScenes(scenes):
    return [x for x in scenes if (x.isAvailable() and (not x.isFinished()))]
