## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    
    class HistoryMenuEntry(renpy.character.HistoryEntry):
        def __init__(self, items):
            super(HistoryMenuEntry, self).__init__()
            self.kind = 'menu'
            self.items = items


    def addMenuHistory(items):
        # 선택지를 히스토리 항목에 추가
        history = renpy.store._history_list # type: ignore

        h = HistoryMenuEntry(items)

        if renpy.game.context().rollback:
            h.rollback_identifier = renpy.game.log.current.identifier # type: ignore
        else:
            h.rollback_identifier = None # type: ignore

        history.append(h)

        while len(history) > renpy.config.history_length:
            history.pop(0)

        return

    # 메뉴 호출시 나타나는 함수
    def menu(items, **add_input):
        """Overwrites the default menu handler, thus allowing us to log the
        choice made by the player.
        The default menu handler is set to renpy.display_menu(), as seen in
        renpy/defaultstore.py.
        Implementation of this is based on delta's readback module."""
        rv = renpy.display_menu(items, **add_input)

        nh = False

        for item_text, choice_obj in items:
            if choice_obj.kwargs.get('noHistory'):
                nh = True
                break

        if nh is False:
            hiEntry = {}

            for item_text, choice_obj in items:
                if rv == choice_obj.value:
                    hiEntry[item_text] = True
                else:
                    hiEntry[item_text] = False
                    
            addMenuHistory(hiEntry)

        return rv


transform choiceVBoxOneButtonHop(p, t, of, ial = .0, hal = .0, sial = 1., shal = 1.):
    xpos p ypos .5 yanchor .5 yoffset 4 alpha ial

    on idle:
        xoffset 0 alpha ial

    on hover:
        alpha hal
        easein t xoffset of
        easeout t xoffset 0
        repeat

    on selected_idle:
        xoffset 0 alpha sial

    on selected_hover:
        alpha shal
        easein t xoffset of
        easeout t xoffset 0
        repeat

define choiceSymbols = "①②③④⑤⑥⑦⑧⑨"
define choiceShortcuts = [ "K_1", "K_2", "K_3", "K_4", "K_5", "K_6", "K_7", "K_8", "K_9" ]
default choiceShortcutPressed = None

screen choiceVBoxOneButton(i, n):
    style_prefix "choiceVBox"
    
    key choiceShortcuts[n]:
        action If(  choiceShortcutPressed==choiceShortcuts[n],
                    i.action,
                    SetVariable("choiceShortcutPressed", choiceShortcuts[n]) )

    button:
        action i.action
        selected choiceShortcutPressed==choiceShortcuts[n]
        hovered SetVariable("choiceShortcutPressed", None)
        unhovered SetVariable("choiceShortcutPressed", None)

        has frame

        xysize (gui.choice_button_width, 32)

        text choiceSymbols[n] at choiceVBoxOneButtonHop(.15, .5, 8, 1., 1.)
        text i.caption xalign .5
        text "√" at choiceVBoxOneButtonHop(.85, .5, -8)

screen choice(items):
    on "show" action SetVariable("choiceShortcutPressed", None)

    style_prefix "choice"

    frame:
        vbox:
            for (n, i) in enumerate(items):
                use choiceVBoxOneButton(i, n)

    use splashQuickMenu()

screen namechoice(items):
    on "show" action SetVariable("choiceShortcutPressed", None)
    
    style_prefix "choice"

    frame:
        vbox:
            align (.5, .5)

            text "{으로=#33F}[persistent.myName]{/으로} 결정하시겠습니까?"
            null height(10)

            for (n, i) in enumerate(items):
                use choiceVBoxOneButton(i, n)

    use splashQuickMenu()

style choice_vbox is vbox
style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_text is text:
    align (.5, .5)
    size 35

style choice_frame is frame:
    pos (gui.textbox_xpos, gui.textbox_ypos) anchor (gui.textbox_xanchor, gui.textbox_yanchor)
    xsize 1280 yminimum 256 yfill False
    padding (10, 20, 10, 60)
    background Frame("gui/choicebox.png", 40, 40, 40, 80)

style choice_vbox:
    spacing gui.choice_spacing
    pos (gui.dialogue_xpos, gui.dialogue_ypos) anchor (gui.dialogue_xanchor, gui.dialogue_yanchor)
    yfill False

style choice_button is default:
    properties gui.button_properties("choice_button")
    xysize (gui.choice_button_width, gui.choice_button_height)

style choice_button_text is default:
    properties gui.text_properties("choice_button")

style choiceVBox_text is default:
    properties gui.text_properties("choice_button")
    idle_color "#000"
    hover_color "#FFF"
    selected_idle_color "#00F"
    selected_hover_color "#EEF"

style choiceVBox_frame is frame:
    xysize (gui.choice_button_width, gui.choice_button_height)
    idle_background "gui/button/choice_idle_background.png"
    hover_background "gui/button/choice_hover_background.png"
    selected_idle_background "gui/button/choice_selected_idle_background.png"
    selected_hover_background "gui/button/choice_hover_background.png"
    padding (0, 0, 0, 0)

