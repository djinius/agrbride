## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen sayNormal(who, what):

    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

        use splashQuickMenu()

screen sayHScene(who, what):
    style_prefix "say"

    window:
        id "window"
        background None

        text what id "what":
            color "#FFF"
            if who is not None:
                outlines [(3, globals()[who].who_args['hcolor'], 1, 1)]
            else:
                outlines [(3, "#000", 1, 1)]
            yalign 1.


screen say(who, what):

    on "show" action SetVariable("afm", what)
    on "hide" action SetVariable("afm", None)

    if gHScene:
        use sayHScene(who, what)
    else:
        use sayNormal(who, what)

## Character 객체를 통해 스타일을 지정할 수 있도록 namebox를 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    pos (gui.textbox_xpos, gui.textbox_ypos) anchor (gui.textbox_xanchor, gui.textbox_yanchor)
    xysize (gui.textbox_width, gui.textbox_height)
    padding (2, 2, 2, 42)

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    padding (5, 5)
    background None # Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    pos (gui.name_xpos, gui.name_ypos) anchor (gui.name_xanchor, gui.name_yanchor) offset (gui.name_xoffset, gui.name_yoffset)
    xminimum 202 yminimum 40
    text_align gui.name_xalign

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    xmaximum gui.dialogue_width
    pos (gui.dialogue_xpos, gui.dialogue_ypos) anchor (gui.dialogue_xanchor, gui.dialogue_yanchor)
    text_align gui.dialogue_text_xalign
    adjust_spacing False

image ctcBlink:
    Animation("gui/ctc_off.png", .5, "gui/ctc_on.png", .5)

image ctcTail:
    "gui/ctc_tail_on.png"
    alpha .0
    block:
        easeout 1. alpha 1.
        easein 1. alpha .0
        repeat

screen ctc:
    add "ctcBlink" align (1., 1.)
