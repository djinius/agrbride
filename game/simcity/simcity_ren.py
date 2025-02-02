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
            gInitialXAlign = ms.scope["citymap"].xadjustment.get_value() / (5120 - 1920)
            gInitialYAlign = ms.scope["citymap"].yadjustment.get_value() / (4096 - 1080)
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

def calcXYPos(x, y, xoff = 0, yoff = 0):
    xp  = x * 256 + 512
    yp  = y * 128 + 2048
    xp += y * 192
    yp -= x * 128


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

def getBuilding(x, y):
    global gCityMap
    return gCityMap[y][x]

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
    newTree = globals()[b](x, y)
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
            ret += b.getWaterSupply()

    return ret

def getTotalWaterDemand():
    global gBuildings

    ret = 0

    for b in gBuildings:
        ret += b.getWaterDemand()

    ret += (getTotalPopulation() + 19) // 20
    return ret

def getAvailableWater():
    return getTotalWaterSupply() - getTotalWaterDemand()

def getShortColor(fa, fb, ec="#000", sc="#F00"):
    if fa() < fb():
        return sc
    else:
        return ec

def addExperience(amount = -1):
    global gExperience
    global gExperienceLevel
    global gFiefLevel

    if gFiefLevel == len(gExperienceLevel):
          return

    if amount == -1:
        amount = gExperienceLevel[gFiefLevel]

    gExperience += amount

    while gExperience >= gExperienceLevel[gFiefLevel]:
        gExperience -= gExperienceLevel[gFiefLevel]
        gFiefLevel += 1

    renpy.restart_interaction()
