"""renpy
init -1 python:
"""

class Building:
    def __init__(self, name, x, y, maxlevel, minimapColor):
        self.x = x
        self.y = y
        self.name = name
        self.level = 1
        self.maxlevel = maxlevel
        self.minimapColor = minimapColor

    def getIdleSprite(self):
        return "images/simcity/buildings/" + self.name + "_level" + str(self.level) + ".png"

    def isUpgradeEnabled(self):
        return self.level < self.maxlevel

    def upgrade(self):
        if self.level < self.maxlevel:
            self.level += 1

    def getMinimapColor(self):
        return self.minimapColor

class AppleTree(Building):
    def __init__(self, x, y):
        super(AppleTree, self).__init__("apple", x, y, 4, "#F88")

class GrapeTree(Building):
    def __init__(self, x, y):
        super(GrapeTree, self).__init__("grape", x, y, 4, "#409")

class TeaTree(Building):
    def __init__(self, x, y):
        super(TeaTree, self).__init__("tea", x, y, 4, "#0F0")

class RiceTree(Building):
    def __init__(self, x, y):
        super(RiceTree, self).__init__("rice", x, y, 4, "#840")

class SharonTree(Building):
    def __init__(self, x, y):
        super(SharonTree, self).__init__("sharon", x, y, 3, "#FF0")

class NymphaTree(Building):
    def __init__(self, x, y):
        super(NymphaTree, self).__init__("nympha", x, y, 3, "#FFF")

