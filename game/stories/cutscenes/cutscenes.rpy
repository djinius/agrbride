default cutscenes = [SunnaWellScene(), RosalindBedScene(), MaliSharonScene()]

label playCutScene(cutSceneObject):

    $ gShowPopupMenu = False
    $ gShowDetails = None
    $ gTargetTree = None
    $ xLoc = None
    $ yLoc = None

    show screen buildit(isManageEnabled = False)

    call expression cutSceneObject.getLabelName()
    $ cutSceneObject.finish()
    $ nextCutScene = None

    hide screen buildit

    return

label sunnaWellScene:

    수나 몬무스 "영지에 나무가 계속 늘어나는구나."
    수나 "그만큼 물도 많이 필요할 게야."
    수나 "우물을 파서 수자원을 확보하거라. 물이 깨끗해야 하니 버드나무도 우물 옆에 함께 심어야겠지."

    return

label maliSharonScene:

    말리 몬무스 "오, 이런 자기."
    말리 "내 열매를 노리고 해충들이 몰려들고 있어."
    말리 "무궁화나무를 심어. 해충들을 소탕할 전초기지가 되어 줄 거야."

    return

