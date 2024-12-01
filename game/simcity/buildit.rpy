default gEdgeScroll = False
default gCityMap = None
default gBuildings = []
default gShowPopupMenu = False
default gShowDetails = None
default gTargetTree = None
default xLoc = None
default yLoc = None
default gInitialXAlign = .0
default gInitialYAlign = 1.

default gPopupUnlocked = False
default gWellUnlocked = False
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

    vbox:
        align (.0, .0)

        frame:
            background Solid("#000")
            ysize 35

            has hbox
            text "인구: %d" % getTotalPopulation()
            text "관리: %d" % getTotalManagements()
            text "대기인력: %d" % getAvailablePopulation()
            text "물 공급: %d" % getTotalWaterSupply()
            text "물 수요: %d" % getTotalWaterDemand()
            text "목재: %d" % gFactory.getWoodStock()

        $ next = availableCutScenes(cutscenes)

        vbox:
            align (.0, .25)

            for s in next:
                button:
                    xysize (150, 50)
                    action [SetVariable("nextCutScene", s), Return()]

                    has frame
                    background None
                    xysize (1., 1.)
                    padding (0, 0)

                    has hbox
                    add "gui/buildit/bubble.png"
                    text s.getTitle() size 25 yalign .5 idle_color "#FFF" hover_color "#FF0"

                    imagebutton:
                        xalign 1.
                        idle "gui/buildit/gift.png"
                        action Function(s.finish)

    if isManageEnabled:
        frame:
            align (1., 1.)
            padding (0, 0)
            background None

            has hbox

            if gFactory.isUnlocked():
                textbutton "공방" action NullAction()

            textbutton "관리 종료" action Return()

    if gFactory.isUnlocked():
        timer 1. repeat True action Function(gFactory.recalcStocks)
    

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