"""renpy
init -1 python:
"""

def say_arguments_callback(char, *args, **kwargs):
    # renpy.sound.play("flashing.mp3")
    return args, kwargs
