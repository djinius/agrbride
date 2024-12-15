default gEdgeScroll = False
default gCityMap = None
default gBuildings = []
default gShowPopupMenu = False
default gShowDetails = None
default gTargetTree = None
default xLoc = None
default yLoc = None
default gInitialXAlign = .0
default gInitialYAlign = .5

default gPopupUnlocked = False
default gResidenceUnlocked = False
default gWellUnlocked = False
default gStatiumUnlocked = False
default gSharonUnlocked = False
default nextCutScene = None

default gAppleTrees = 0
default gGrapeTrees = 0
default gPeachTrees = 0

default gSupplyDepots = 0
default gFiefLevel = 1
default gExperience = 0

define gExperienceLevel = [x*100 for x in range(0, 62)]

default gFactory = Factory()

transform upgradeBubble:
    on idle:
        yoffset -120

    on hover:
        easein .5 yoffset -130
        easeout .5 yoffset -120
        repeat


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
        if gEdgeScroll and isManageEnabled:
            edgescroll (200, 200)
            
        draggable True
        mousewheel True
        xinitial gInitialXAlign yinitial gInitialYAlign

        frame:
            xysize (5120, 4096)
            background "gamemadang/map.png"

            for y, row in enumerate(gCityMap):
                for x, b in enumerate(row):
                    if b is not None:
                        imagebutton:
                            idle b.getIdleSprite()
                            pos calcXYPos(x, y) anchor (1., 1.)
                            action SetVariable("gShowDetails", b)
                            alternate Function(setBuilding, x=x, y=y, p=b)
                            sensitive isManageEnabled

                        # 업그레이드 자원 표기
                        if b.upgradeResources is not None:
                            imagebutton:
                                idle "gui/buildit/bubble.png"
                                pos calcXYPos(x, y) anchor (.75, .75)
                                at upgradeBubble

                                if b.isUpgradeAvailable():
                                    action Function(b.upgrade)
                                else:
                                    action NullAction()

                    else:
                        imagebutton:
                            idle "images/simcity/empty.png"
                            pos calcXYPos(x, y) anchor (1., 1.) focus_mask True
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
        has vbox

        if gFiefLevel == 61:
            text "특급 영지"
        else:
            hbox:
                text "%d등급 영지" % gFiefLevel yalign 1.
                bar value AnimatedValue(value = gExperience, range = gExperienceLevel[gFiefLevel]) xysize (300, 25) yalign 1.

        hbox:
            text "수용 가능 인구: %d" % getAcceptablePopulation()
            text "식량: %d" % getTotalFoodSupply()
            text "총 인구: %d" % getTotalPopulation() color getShortColor(getTotalFoodSupply, getTotalPopulation)
            text "관리인력: %d" % getTotalManagements() color getShortColor(getTotalPopulation, getTotalManagements)
            text "물: %d/%d" % (getTotalWaterDemand(), getTotalWaterSupply()) color getShortColor(getTotalWaterSupply, getTotalWaterDemand)
            text "목재: %d/%d" % (gFactory.getWoodStock(), gFactory.getMaxWoodStock())


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

        timer 1. repeat True action Function(manageBuildings)
    
        $ next = availableCutScenes(cutscenes)

        if next:
            timer .1 action [SetVariable("nextCutScene", next[0]), Return()]

screen builditPopup(xloc, yloc):
    frame:
        pos calcXYPos(xloc, yloc) anchor (1., 1.) offset (-64, -64)

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
            action [Function(addBuilding, x=xloc, y=yloc, b="AppleTree"), Function(setLocation, x=None, y=None, p=False)]
            sensitive ((getTotalPopulation() > getTotalManagements()) and (getTotalAppleTrees() < gFiefLevel * 2)) or ((getTotalAppleTrees() < 2))
            text_size 25

        if gResidenceUnlocked:
            textbutton "거주구":
                action [Function(addBuilding, x=xloc, y=yloc, b="Residence"), Function(setLocation, x=None, y=None, p=False)]
                text_size 25

        if gWellUnlocked:
            textbutton "우물":
                action [Function(addBuilding, x=xloc, y=yloc, b="Well"), Function(setLocation, x=None, y=None, p=False)]
                text_size 25

        if gSharonUnlocked:
            textbutton "무궁화":
                action [Function(addBuilding, x=xloc, y=yloc, b="SharonTree"), Function(setLocation, x=None, y=None, p=False)]
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