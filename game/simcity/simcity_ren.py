"""renpy
init -1 python:
"""

import pygame

###############################################################################
# 미니맵 프레임 위치
###############################################################################

class CityMapFrame(renpy.Displayable):
    def __init__(self, **kwargs):

        # Pass additional properties on to the renpy.Displayable
        # constructor.
        super(CityMapFrame, self).__init__(**kwargs)
        self.isDragging = False

    def render(self, width, height, st, at):
        render = renpy.Render(0, 0)
        # Return the render.
        return render

    def event(self, ev, x, y, st):
        global gInitialXAlign
        global gInitialYAlign

        ms = renpy.get_screen("buildit")

        if ev.type == pygame.MOUSEBUTTONDOWN:
            self.isDragging = True

        elif ev.type == pygame.MOUSEBUTTONUP:
            self.isDragging = False

        elif ev.type == pygame.MOUSEMOTION:
            gInitialXAlign = (ms.scope["citymap"].xadjustment.get_value() - 1920) / 6000.
            gInitialYAlign = ms.scope["citymap"].yadjustment.get_value() / (6000. - 1080)
            renpy.restart_interaction()

        return None


def initBuildings():
    global gCityMap

    gCityMap = []

    for y in range(0, 16):
        row = []
        for x in range(0, 20):
            row.append(None)
        gCityMap.append(row)

def calcXYPos(x, y):
    xp = x * 200 + 320
    yp = y * 328 + 320

    return (xp, yp)

def setLocation(x, y, p):
    global xLoc
    global yLoc
    global gShowPopupMenu
    global gTargetTree
    global gShowDetails

    xLoc = x
    yLoc = y
    gShowPopupMenu = p
    gTargetTree = None
    gShowDetails = None

def setBuilding(x, y, p):
    global xLoc
    global yLoc
    global gShowPopupMenu
    global gTargetTree

    xLoc = None
    yLoc = None
    gShowPopupMenu = False
    gTargetTree = p

def addBuilding(x, y, b):
    global gBuildings

    if b == "apple":
        newTree = AppleTree(x, y)
    elif b == "grape":
        newTree = GrapeTree(x, y)
    elif b == "well":
        newTree = Well(x, y)
    else:
        pass

    renpy.restart_interaction()

def placeBuilding(x, y, b):
    global gCityMap
    gCityMap[y][x] = b

def appendBuilding(b):
    global gBuildings
    gBuildings.append(b)

def removeBuilding(b):
    global gBuildings
    global gCityMap

    placeBuilding(b.x, b.y, None)
    gBuildings.remove(b)

def getTotalWaterSupply():
    global gBuildings

    ret = 50

    for b in gBuildings:
        if isinstance(b, Well):
            ret += 100

    return ret

def getTotalWaterDemand():
    global gBuildings

    ret = 0
    pop = getTotalPopulation()

    for b in gBuildings:
        ret += b.getWaterDemand()

    ret += getTotalPopulation() // 50
    return ret

def getAvailableWater():
    return getTotalWaterSupply() - getTotalWaterDemand()
