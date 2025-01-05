# Auto: (4, 0, 68, 38)
# Fast: (72, 0, 68, 38)
# Skip: (140, 0, 68, 38)

# -- in play
# Save: (208, 0, 68, 38)
# Load: (276, 0, 68, 38)

# -- in replay
# Return: (208, 0, 78, 38)

# Replay: (402, 0, 78, 38)

# Hide: (480, 0, 68, 38)

screen splashQuickMenu():
    imagemap:
        pos (1., 1.) anchor (1., .0) offset (-50, 2)
        alpha False
        if _in_replay:
            auto "gui/quickmenu/replay_%s.png"
        else:
            auto "gui/quickmenu/inplay_%s.png"
            hotspot (4, 0, 68, 38) action Preference("auto-forward", "toggle")
            hotspot (72, 0, 68, 38) action Skip()
            hotspot (140, 0, 68, 38) action Skip(fast=True)
            hotspot (208, 0, 68, 38) action ShowMenu("save")
            hotspot (276, 0, 68, 38) action ShowMenu("load")
            hotspot (402, 0, 78, 38) action VoiceReplay()
            hotspot (480, 0, 68, 38) action HideInterface()
