"""renpy
init -1 python:
"""

def say_arguments_callback(char, *args, **kwargs):
    # renpy.sound.play("flashing.mp3")
    return args, kwargs

def getAvailableDates():
    global gDates
    p = getIdlePopulation() // 1000

    return min(max(0, p - gDates), 120)


def isDateAvailable():
    return getAvailableDates() > 0
