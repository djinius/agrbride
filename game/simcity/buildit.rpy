default gEdgeScroll = False
default gBuildings = None
default gShowPopupMenu = False
default xLoc = None
default yLoc = None
default gInitialXAlign = .0
default gInitialYAlign = 1.
default gNextLabel = None

screen buildit():
    add CityMapFrame()

    viewport id "vp" as citymap:
        if gEdgeScroll:
            edgescroll (200, 400)
            
        draggable True
        mousewheel True
        xinitial gInitialXAlign yinitial gInitialYAlign

        frame:
            xysize (3840, 2176)
            background "simcity/map.png"

            for y, row in enumerate(gBuildings):
                for x, b in enumerate(row):
                    if b is not None:
                        imagebutton:
                            auto "images/simcity/buildings/" + b + "_tile_%s_bg.png"
                            pos calcXYPos(x, y)
                            action NullAction()
                    else:
                        imagebutton:
                            idle Solid("#0000")
                            hover Solid("#F008")
                            selected_idle Solid("#8F08")
                            selected_hover Solid("#FF08")
                            xysize (128, 128)
                            pos calcXYPos(x, y)
                            selected xLoc==x and yLoc==y
                            action Function(setLocation, x=x, y=y, p=True)
        
            if (xLoc is not None) and (yLoc is not None) and gShowPopupMenu:
                use builditPopup(xLoc, yLoc)

    frame:
        xysize (300, 170) align (.0, 1.)
        padding (0, 0)
        background Solid("#000")

        for y, row in enumerate(gBuildings):
            for x, b in enumerate(row):
                if b == "apple":
                    add Solid("#F88") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)
                elif b == "grape":
                    add Solid("#409") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)
                elif b == "tea":
                    add Solid("#0F0") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)
                elif b == "rice":
                    add Solid("#840") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)
                elif b == "sharon":
                    add Solid("#FF0") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)
                elif b == "nympha":
                    add Solid("#FFF") xysize (10, 10) pos (x*10+30, y*10) anchor (.0, .0)

        add Frame("images/simcity/minimap_border.png", 5, 5):
            xysize (150, 85)
            align (gInitialXAlign, gInitialYAlign)

    frame:
        align (1., 1.)
        padding (0, 0)
        background None

        has hbox
        add "rosalind_councelor"
        add "mali_councelor"
        add "cera_councelor"
        add "chara_councelor"
        add "coggi_councelor"
        add "erga_councelor"
        add "lucy_councelor"
        add "manda_councelor"

    key "game_menu" action [SetVariable("gNextLabel", "gameMenu"), Return()]

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
        textbutton "닫기":
            action Function(setLocation, x=None, y=None, p=False)
            text_size 25

