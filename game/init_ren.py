"""renpy
init python:
"""
def adjustKeymap():
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['game_menu'].remove('mouseup_3')

    # customizing keymap
    config.keymap['self_voicing'].clear()
    config.keymap['screenshot'] = ['K_F12']
    config.keymap['toggle_fullscreen'].remove('noshift_K_f')
    config.keymap['toggle_afm'].append('noshift_K_a')
    config.keymap['toggle_skip'].append('noshift_K_f')
    config.keymap['fast_skip'].append('noshift_K_k')
    config.keymap['fast_skip'].append('K_END')
    config.keymap['rollback'].clear()
    config.keymap['rollforward'].clear()
    config.keymap['quicksave'] = ['noshift_K_q']

# 매 게임마다 초기화하는 코드를 여기에 넣기
renpy.music.register_channel("sound2", "sfx")
renpy.music.register_channel("sound3", "sfx")

adjustKeymap()

# config.keymap['hide_windows'] = ['noshift_K_h']
# config.keymap['save'] = ['noshift_K_s']
# mousedown_4, mousedown_5

# s for save
custom_keymap = renpy.Keymap(screenshot = MyScreenshot(), quicksave=MyQuickSave())
config.underlay.append(custom_keymap)
