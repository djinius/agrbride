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

screen splashQuickMenu(hscene = False):
    if hscene is False:
        imagemap:
            pos (gui.textbox_xpos, gui.textbox_ypos) anchor (gui.textbox_xanchor, gui.textbox_yanchor)
            offset (280, -2)
            alpha False

            if _in_replay:
                auto "gui/quickmenu/replay_%s.png"
                hotspot (4, 0, 68, 38) action Preference("auto-forward", "toggle")
                hotspot (72, 0, 68, 38) action Skip()
                hotspot (140, 0, 68, 38) action Skip(fast=True)
                hotspot (208, 0, 78, 38) action EndReplay(confirm=False)
                hotspot (402, 0, 78, 38) action VoiceReplay()
                hotspot (480, 0, 68, 38) action HideInterface()
                hotspot (575, 0, 30, 38) action ShowMenu("preferences")
                hotspot (605, 0, 30, 38) action ToggleField(persistent, "isStreaming")

            else:
                auto "gui/quickmenu/inplay_%s.png"
                hotspot (4, 0, 68, 38) action Preference("auto-forward", "toggle")
                hotspot (72, 0, 68, 38) action Skip()
                hotspot (140, 0, 68, 38) action Skip(fast=True)
                hotspot (208, 0, 68, 38) action ShowMenu("save") sensitive _in_gameplay
                hotspot (276, 0, 68, 38) action ShowMenu("load") sensitive _in_gameplay
                hotspot (402, 0, 78, 38) action VoiceReplay()
                hotspot (480, 0, 68, 38) action HideInterface()
                hotspot (575, 0, 30, 38) action ShowMenu("preferences")
                hotspot (605, 0, 30, 38) action ToggleField(persistent, "isStreaming")

            if persistent.sayScreenAlpha < 50:
                ground "gui/quickmenu/ground_transparent.png"
            else:
                ground "gui/quickmenu/ground.png"

    if _in_replay:
        pass
    elif _in_gameplay:
        key 'noshift_K_s' action ShowMenu("save")
        key 'noshift_K_l' action ShowMenu("load")

    if persistent.scrollFunction == 0:
        if _in_gameplay or _in_replay:
            key "mousedown_4" action ShowMenu("history")
            key "mousedown_5" action ShowMenu("history")
    elif persistent.scrollFunction == 1:
        if _in_gameplay or _in_replay:
            key "mousedown_4" action ShowMenu("history")
        key "mousedown_5" action QueueEvent('dismiss')
    elif persistent.scrollFunction == 2:
        key "mousedown_4" action Rollback()
        key "mousedown_5" action QueueEvent('dismiss')
