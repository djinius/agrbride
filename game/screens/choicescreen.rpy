## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    def getChoiceWidth(items):
        global gui

        ln = len(items)

        w = int( (1280 - gui.choice_spacing * (ln - 1)) / ln )
        print( "choice button size: ", ln, w )
        return w

transform choiceVBoxOneButtonHop(p, t, of):
    xpos p ypos .5 yanchor .5

    on idle:
        xoffset 0

    on hover:
        easein t xoffset of
        easeout t xoffset 0
        repeat

screen choiceVBoxOneButton(i):
    style_prefix "choiceVBox"
    
    button:
        action i.action

        has frame

        xsize gui.choice_button_width
        text "▶" at choiceVBoxOneButtonHop(.15, .5, 8)
        text i.caption xalign .5
        text "◀" at choiceVBoxOneButtonHop(.85, .5, -8)


screen choice(items):
    style_prefix "choice"

    frame:
        has vbox
        for i in items:
            use choiceVBoxOneButton(i)

style choice_vbox is vbox
style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_frame is frame:
    pos (gui.textbox_xpos, gui.textbox_ypos) anchor (gui.textbox_xanchor, gui.textbox_yanchor)
    xysize (1280, 256)
    padding (0, 0, 0, 0)
    background "gui/textbox.png"

style choice_vbox:
    spacing gui.choice_spacing
    pos (gui.dialogue_ypos, gui.dialogue_ypos) anchor (gui.dialogue_xanchor, gui.dialogue_yanchor)

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

style choiceVBox_text is default:
    properties gui.text_properties("choice_button")
    idle_color "#000"
    hover_color "#FFF"

style choiceVBox_frame is frame:
    xysize (gui.choice_button_width, gui.choice_button_height)
    idle_background "gui/button/choice_idle_background.png"
    hover_background "gui/button/choice_hover_background.png"
    padding (0, 0, 0, 0)

