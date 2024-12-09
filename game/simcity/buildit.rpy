default gEdgeScroll = False
default gCityMap = None
default gBuildings = []
default gShowPopupMenu = False
default gShowDetails = None
default gTargetTree = None
default xLoc = None
default yLoc = None
default gInitialXAlign = .0
default gInitialYAlign = .0

default gPopupUnlocked = False
default gWellUnlocked = False
default gStatiumUnlocked = False
default gSharonUnlocked = False
default nextCutScene = None

default gFactory = Factory()

###############################################################################
#
# 파라미터
#
# 식량 생산량
# 물 공급량
# 하수 처리량
# 
###############################################################################

screen buildit(isManageEnabled = True):
    add CityMapFrame()
    style_prefix "buildit"

    default factoryPopup = False

    if isManageEnabled:
        key "game_menu" action NullAction()

    viewport id "vp" as citymap:
        if gEdgeScroll:
            edgescroll (200, 400)
            
        draggable True
        mousewheel True
        xinitial gInitialXAlign yinitial gInitialYAlign

        frame:
            xysize (6000, 6000)
            background "simcity/map.png"

            for y, row in enumerate(gCityMap):
                for x, b in enumerate(row):
                    if b is not None:
                        imagebutton:
                            idle b.getIdleSprite()
                            pos calcXYPos(x, y) anchor (.5, .5)
                            action SetVariable("gShowDetails", b)
                            alternate Function(setBuilding, x=x, y=y, p=b)
                            sensitive isManageEnabled

                    else:
                        imagebutton:
                            idle "images/simcity/buildings/empty.png"
                            pos calcXYPos(x, y) anchor (.5, .5) focus_mask True
                            selected xLoc==x and yLoc==y
                            action [SetVariable("gTargetTree", None), SetVariable("gShowDetails", None), Function(setLocation, x=x, y=y, p=True)]
                            alternate Function(setLocation, x=x, y=y, p=True)
                            sensitive gPopupUnlocked and isManageEnabled
        
            if (xLoc is not None) and (yLoc is not None) and isManageEnabled:
                if gShowPopupMenu:
                    use builditPopup(xLoc, yLoc)
            elif (gTargetTree is not None) and isManageEnabled:
                use buildingPopup(gTargetTree)
            elif (gShowDetails is not None) and (gShowDetails.getDetailScreen() is not None) and isManageEnabled:
                use expression gShowDetails.getDetailScreen() pass (b=gShowDetails)

    frame:
        align (.0, 1.)
        background None

        has hbox

        text "식량: %d" % getTotalPopulation()
        text "관리인력: %d" % getTotalManagements()
        text "대기인력: %d" % getAvailablePopulation()
        text "물 공급: %d" % getTotalWaterSupply()
        text "물 수요: %d" % getTotalWaterDemand()
        text "목재: %d" % gFactory.getWoodStock()


    if isManageEnabled:
        if gFactory.isUnlocked() and factoryPopup:
            frame:
                align (1., 1.) offset (-100, -30)
                background None
                xysize (300, 300)

                has vbox

                text "공방"
                text "%d등급" % gFactory.level
                textbutton "등급 향상" action Function(gFactory.upgrade) sensitive gFactory.isUpgradeAvailable()

        frame:
            align (1., 1.)
            padding (0, 0)
            background None

            has hbox

            textbutton "공방" action ToggleLocalVariable("factoryPopup") sensitive gFactory.isUnlocked()

            textbutton "관리 종료" action Return()

        if gFactory.isUnlocked():
            timer 1. repeat True action Function(gFactory.recalcStocks)
    
        $ next = availableCutScenes(cutscenes)

        if next:
            timer .1 action [SetVariable("nextCutScene", next[0]), Return()]

screen builditPopup(xloc, yloc):
    frame:
        pos calcXYPos(xloc, yloc) offset (64, 64)

        if xloc >= (25):
            xanchor 1.
        else:
            xanchor 0.

        if yloc >= (14):
            yanchor 1.
        else:
            yanchor 0.

        has vbox
        textbutton "사과나무":
            action [Function(addBuilding, x=xloc, y=yloc, b="apple"), Function(setLocation, x=None, y=None, p=False)]
            sensitive getAvailableWater() > 7
            text_size 25

        if gWellUnlocked:
            textbutton "우물":
                action [Function(addBuilding, x=xloc, y=yloc, b="well"), Function(setLocation, x=None, y=None, p=False)]
                text_size 25

        if gSharonUnlocked:
            textbutton "무궁화":
                action [Function(addBuilding, x=xloc, y=yloc, b="sharon"), Function(setLocation, x=None, y=None, p=False)]
                text_size 25

screen buildingPopup(b):
    frame:
        pos calcXYPos(b.x, b.y) offset (64, 64) anchor (1., 1.)

        has vbox

        text b.localName
        null height(3)

        $ cm = b.getContextMenu()
        for i in cm:
            textbutton i:
                sensitive cm[i][1]()
                action [Function(cm[i][0]), Function(setLocation, x=None, y=None, p=False)]
                text_size 25

        null height(5)
        textbutton "이동":
            action Function(setLocation, x=None, y=None, p=False)
            text_size 25
        textbutton "닫기":
            action Function(setLocation, x=None, y=None, p=False)
            text_size 25

screen fruitTreeDetails(b):
    frame:
        pos calcXYPos(b.x, b.y) offset (64, 64) anchor (1., 1.)

        has hbox
        add b.getIdleSprite() zoom 2.

        vbox:
            yalign .0
            $ cm = b.getContextMenu()
            for i in cm:
                textbutton i:
                    sensitive cm[i][1]()
                    action Function(cm[i][0])
                    text_size 25

            null height(5)
            textbutton "닫기":
                action SetVariable("gShowDetails", None)
                text_size 25

style buildit_hbox:
    spacing 10

style buildit_text:
    size 25