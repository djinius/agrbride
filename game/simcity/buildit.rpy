default gEdgeScroll = False
default gCityMap = None
default gBuildings = []
default gShowPopupMenu = False
default gTargetTree = None
default xLoc = None
default yLoc = None
default gInitialXAlign = .0
default gInitialYAlign = 1.
default gNextLabel = None

screen buildit():
    add CityMapFrame()

    key "game_menu" action NullAction()

    viewport id "vp" as citymap:
        if gEdgeScroll:
            edgescroll (200, 400)
            
        draggable True
        mousewheel True
        xinitial gInitialXAlign yinitial gInitialYAlign

        frame:
            xysize (3840, 2176)
            background "simcity/map.png"

            for y, row in enumerate(gCityMap):
                for x, b in enumerate(row):
                    if b is not None:
                        imagebutton:
                            if isinstance(b, Building):
                                idle b.getIdleSprite()
                            pos calcXYPos(x, y)
                            action NullAction()
                            alternate Function(setBuilding, x=x, y=y, p=b)
                    else:
                        imagebutton:
                            idle "images/simcity/buildings/empty.png"
                            pos calcXYPos(x, y)
                            selected xLoc==x and yLoc==y
                            action Function(setLocation, x=x, y=y, p=True)
                            alternate Function(setLocation, x=x, y=y, p=True)
        
            if (xLoc is not None) and (yLoc is not None):
                if gShowPopupMenu:
                    use builditPopup(xLoc, yLoc)
                elif gTargetTree is not None:
                    use buildingPopup(xLoc, yLoc, gTargetTree)

    frame:
        xysize (300, 170) align (.0, 1.)
        padding (0, 0)
        background Solid("#000")

        for y, row in enumerate(gCityMap):
            for x, b in enumerate(row):
                if b is not None:
                    add Solid(b.getMinimapColor()) xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)

        add Frame("images/simcity/minimap_border.png", 5, 5):
            xysize (150, 85)
            align (gInitialXAlign, gInitialYAlign)

    frame:
        align (1., 1.)
        padding (0, 0)
        background None

        has hbox
        textbutton "닫기" action Return()
        add "rosalind_advisor"
        add "mali_advisor"
        add "cera_advisor"
        add "chara_advisor"
        add "coggi_advisor"
        add "erga_advisor"
        add "lucy_advisor"
        add "manda_advisor"

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
            text_size 25
        textbutton "포도나무":
            action [Function(addBuilding, x=xloc, y=yloc, b="grape"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "차나무":
            action [Function(addBuilding, x=xloc, y=yloc, b="tea"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "쌀나무":
            action [Function(addBuilding, x=xloc, y=yloc, b="rice"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "무궁화":
            action [Function(addBuilding, x=xloc, y=yloc, b="sharon"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "각시수련":
            action [Function(addBuilding, x=xloc, y=yloc, b="nympha"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "벌집":
            action [Function(addBuilding, x=xloc, y=yloc, b="hive"), Function(setLocation, x=None, y=None, p=False)]
            text_size 25
        textbutton "닫기":
            action Function(setLocation, x=None, y=None, p=False)
            text_size 25

screen buildingPopup(xloc, yloc, b):
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
