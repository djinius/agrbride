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

def setborder(enable):
    sdl_dll = renpy.exports.platformexports.get_sdl_dll()
    if sdl_dll is None:
        return
    window_ptr = renpy.exports.platformexports.get_sdl_window_pointer()
    if window_ptr is None:
        return
    sdl_dll.SDL_SetWindowBordered(window_ptr, enable)

def maximize():
    sdl_dll = renpy.exports.platformexports.get_sdl_dll()
    if sdl_dll is None:
        return
    window_ptr = renpy.exports.platformexports.get_sdl_window_pointer()
    if window_ptr is None:
        return
    # sdl_dll.SDL_MaximizeWindow(window_ptr)
    sdl_dll.SDL_SetWindowFullscreen(window_ptr, 0x00000001)
