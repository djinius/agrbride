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
            gInitialXAlign = ms.scope["citymap"].xadjustment.get_value() / 1920.
            gInitialYAlign = ms.scope["citymap"].yadjustment.get_value() / 1088.
            renpy.restart_interaction()

        return None


def initBuildings():
    global gBuildings

    gBuildings = []

    for y in range(0, 16):
        row = []
        for x in range(0, 27):
            row.append(None)
        gBuildings.append(row)

        print(y)


def calcXYPos(x, y):
    return (384 + x * 128, y * 128)

def setLocation(x, y, p):
    global xLoc
    global yLoc
    global gShowPopupMenu

    xLoc = x
    yLoc = y
    gShowPopupMenu = p

def addBuilding(x, y, b):
    global gBuildings
    gBuildings[y][x] = b
    renpy.restart_interaction()
