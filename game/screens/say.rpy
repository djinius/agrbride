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

screen sayNormal(who, what, hcolor='#FFF', bg='gui/textbox.png'):

    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    style_prefix "say"

    window:
        id "window"
        background Transform(bg, alpha=(persistent.sayScreenAlpha / 100.))

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    if persistent.sayScreenAlpha < 50:
                        outlines [(2, hcolor, 1, 1)]
                    else:
                        pass


        text what id "what":
            if persistent.sayScreenAlpha < 50:
                color "#FFF"
                outlines [(3, hcolor, 1, 1)]
            else:
                pass

        use splashQuickMenu(hscene = False)

screen sayHScene(who, what, hcolor="#444"):
    style_prefix "say"

    window:
        id "window"
        background None

        text what id "what":
            color "#FFF"
            outlines [(3, hcolor, 1, 1)]
                
            yalign 1.

        use splashQuickMenu(hscene = True)

screen sayCommon(who, what, hcolor="#666", bg='gui/textbox.png'):
    if gHScene:
        use sayHScene(who, what, hcolor)
    else:
        use sayNormal(who, what, hcolor, bg)

screen say(who, what):
    use sayCommon(who, what)

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

image ctc35Blink:
    ConditionSwitch("gHScene", Animation("gui/ctc35_off.png", .5, "gui/ctc35_on.png", .5),
                    "True", Text(""))
    yoffset 7

screen ctc:
    if persistent.ctcDetail and (not gHScene):
        add "ctcBlink" pos (1590, 1020) anchor (1., 1.)
    else:
        pass
