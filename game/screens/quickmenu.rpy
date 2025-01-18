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
            hotspot (4, 0, 68, 38) action Preference("auto-forward", "toggle")
            hotspot (72, 0, 68, 38) action Skip()
            hotspot (140, 0, 68, 38) action Skip(fast=True)
            hotspot (208, 0, 78, 38) action EndReplay(confirm=False)
            hotspot (402, 0, 78, 38) action VoiceReplay()
            hotspot (480, 0, 68, 38) action HideInterface()
            hotspot (550, 0, 30, 38) action ToggleField(persistent, "isStreaming")

        else:
            auto "gui/quickmenu/inplay_%s.png"
            hotspot (4, 0, 68, 38) action Preference("auto-forward", "toggle")
            hotspot (72, 0, 68, 38) action Skip()
            hotspot (140, 0, 68, 38) action Skip(fast=True)
            hotspot (208, 0, 68, 38) action ShowMenu("save") sensitive _in_gameplay
            hotspot (276, 0, 68, 38) action ShowMenu("load") sensitive _in_gameplay
            hotspot (402, 0, 78, 38) action VoiceReplay()
            hotspot (480, 0, 68, 38) action HideInterface()
            hotspot (550, 0, 30, 38) action ToggleField(persistent, "isStreaming")

    if _in_replay:
        pass
    elif _in_gameplay:
        key "S" action ShowMenu("save")
        key "s" action ShowMenu("save")
        key "L" action ShowMenu("load")
        key "l" action ShowMenu("load")

    if _in_gameplay or _in_replay:
        if persistent.isScrollLog:
            key "mousedown_4" action ShowMenu("history")
            key "mousedown_5" action ShowMenu("history")
        else:
            key "mouseup_2" action ShowMenu("history")
