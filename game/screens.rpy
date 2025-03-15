################################################################################
## 초기화
################################################################################

init offset = -1


################################################################################
## 스타일
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 게임내 스크린
################################################################################

## Input 스크린 ###################################################################
##
## 플레이어 입력을 받는 renpy.input을 출력할 때 쓰이는 스크린입니다. prompt 매개
## 변수를 통해 입력 지문을 표시할 수 있습니다.
##
## 이 스크린은 id "input"을 가진 input 디스플레이어블을 생성해야 합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

################################################################################
## Main과 Game Menu 스크린
################################################################################

## Navigation 스크린 ##############################################################
##
## 이 스크린은 메인메뉴와 게임외 메뉴에 포함되어 다른 메뉴로 이동하거나 게임을
## 시작/종료할 수 있게 합니다.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("시작하기") action Start()

        else:

            textbutton _("대사록") action ShowMenu("history")

            textbutton _("저장하기") action ShowMenu("save") sensitive _in_gameplay

        textbutton _("불러오기") action ShowMenu("load")

        textbutton _("환경설정") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("메인 메뉴") action MainMenu()

        textbutton _("버전정보") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## 도움말 메뉴는 모바일 디바이스와 맞지 않아 불필요합니다.
            textbutton _("조작방법") action ShowMenu("help")

        if renpy.variant("pc"):

            ## iOS에서는 종료 버튼이 금지되어 있으며 Android 및 웹에서는 불필요
            ## 합니다.
            textbutton _("종료하기") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu 스크린 ###############################################################
##
## 렌파이가 시작할 때 메인메뉴를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 이렇게 하면 다른 메뉴 화면이 모두 교체됩니다.
    tag menu

    # add gui.main_menu_background
    add "palaceGarden":
        align (.5, .5)
    add "효주 정면 한복":
        pos (.70, .15) anchor (.5, .0)
        zoom .3
    add "말리 정면 한복":
        pos (.85, .15) anchor (.5, .0)
        zoom .3
    add "로잘린드 정면 장옷":
        pos (.5, 0) anchor (.5, .0)
        zoom .75

    ## 이 빈 프레임은 기본 메뉴를 어둡게 만듭니다.
    frame:
        style "main_menu_frame"

    ## use 명령어로 스크린 내에 다른 스크린을 불러옵니다. 메인 메뉴 스크린의 내
    ## 용물은 navigation 스크린에 있습니다.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu 스크린 ###############################################################
##
## 게임 메뉴의 기본 틀입니다. 매개변수 title로 스크린 제목을 정하고, 배경, 제목,
## 그리고 navigation 스크린을 출력합니다.
##
## scroll 매개변수는, None, "viewport" 혹은 "vpgrid" 중 하나여야 합니다.
## transclude 명령어를 통해 다른 스크린을 이 스크린 내부에 불러옵니다.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    #if main_menu:
    #    add gui.main_menu_background
    #else:
    #    # add gui.game_menu_background
    #    pass

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 탐색 섹션을 위한 공간 예약.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("돌아가기"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About 스크린 ###################################################################
##
## 이 스크린은 게임과 렌파이 엔진 크레딧과 저작권 정보를 표시합니다.
##
## 특별할 것이 없으므로 스크린을 새로 커스터마이징하여 만드는 예제이기도 합니다.

screen about():

    tag menu

    ## 이 use 명령어로 game_menu 스크린을 이 스크린 내에 불러옵니다. use 명령어
    ## 하위블럭(vbox 내용)은 game_menu 스크린 내 transclude 명령어가 있는 곳에
    ## 다시 불려집니다.
    use game_menu(_("버전정보"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("버전 [config.version!t]\n")

            ## gui.about 의 내용은 보통 options.rpy에 있습니다.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load 그리고 Save 스크린 ###########################################################
##
## 이 스크린은 세이브/로드에 쓰입니다. 거의 동일하기 때문에, file_slots 스크린을
## 불러와서 씁니다.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("저장하기"))


screen load():

    tag menu

    use file_slots(_("불러오기"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} 페이지"), auto=_("자동 세이브"), quick=_("퀵세이브"))

    use game_menu(title):

        fixed:

            ## input이 세이브/로드 버튼보다 먼저 엔터에 반응하도록 합니다.
            order_reverse True

            ## 페이지 제목을 플레이어가 수정할 수 있음.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 파일 슬롯 그리드.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("빈 슬롯")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 페이지 이동 버튼.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}자동") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}퀵") action FilePage("quick")

                    ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("동기화 업로드"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("동기화 다운로드"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Help 스크린 ####################################################################
##
## 입력장치의 기능을 설명합니다. 각 입력장치별 설정은 keyboard_help, mouse_help,
## gamepad_help 스크린을 각각 불러와서 출력합니다.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("숫자키 1-9")
        text _("선택지 고르기. 두 번 누르면 선택지 선택.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("F, 탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("저장 화면.")

    hbox:
        label "L"
        text _("불러오기 화면.")

    hbox:
        label "Q"
        text _("퀵세이브.")

    hbox:
        label "A"
        text _("자동 진행.")

    hbox:
        label "K"
        text _("다음 선택지, 혹은 장면 끝까지 건너뛰기.")


screen mouse_help():
    use preferencesScrollFunction()

screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("왼쪽 트리거\n왼쪽 어깨")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 그 외 스크린
################################################################################


## Confirm 스크린 #################################################################
##
## 게임 입력 관련 예/아니오 질문을 플레이어에게 할 때 이 스크린을 표시합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 이 스크린이 출력 중일 때 다른 스크린과 상호작용할 수 없게 합니다.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("네") action yes_action
                textbutton _("아니오") action no_action

    ## 우클릭과 esc는 '아니오'를 입력하는 것과 같습니다.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#000"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator 스크린 ##########################################################
##
## Skip_indicator 스크린은 스킵 중일 때 "스킵 중"을 표시하기 위해 출력됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("넘기는 중")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 이 transform으로 화살표를 순서대로 페이드인/페이드아웃합니다.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## BLACK RIGHT-POINTING SMALL TRIANGLE 글리프가 있는 글꼴을 사용해야 합니다.
    font "DejaVuSans.ttf"


## Notify 스크린 ##################################################################
##
## Notify 스크린으로 플레이어에게 메시지를 출력합니다. (예를 들어 '퀵세이브 완
## 료'나 '스크린샷 저장 완료')
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 스크린 #####################################################################
##
## NVL모드 대사와 선택지를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## vpgrid나 vbox 내에 대사를 출력합니다.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 주어진 경우 메뉴를 표시합니다. config.narrator_menu가 True로 설정된
        ## 경우 메뉴가 잘못 표시될 수 있습니다.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 동시에 출력될 수 있는 NVL 대사의 최대치를 조정합니다.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## 말풍선 화면은 말풍선을 사용할 때 플레이어에게 대화를 표시하는 데 사용됩니다.
## 말풍선 화면은 말풍선 화면과 동일한 매개변수를 사용하며, "what" 아이디로 표시
## 가능 항목을 생성해야 하며, "namebox", "who", "window" 아이디로 표시 가능 항목
## 을 생성할 수 있습니다.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 모바일 버전
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 마우스가 없고 화면이 작을 가능성이 높으므로, 퀵메뉴 버튼의 크기를 키우고 가짓
## 수를 줄입니다.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
