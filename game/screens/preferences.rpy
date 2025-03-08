## Preferences 스크린 #############################################################
##
## Preferences 스크린에서는 각종 환경설정을 플레이어가 지정할 수 있습니다.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

## 마우스 기능 선택 #############################################################
##
## 좌클릭: 대사 진행 (기본값, 변경 불가)
## 우클릭: 게임 메뉴 불러오기(기본값) / UI 숨기기
## 스크롤 업: 대사록 불러오기(기본값) / 대사 되돌리기
## 스크롤 다운: 대사록 불러오기 / 대사 진행(기본값)
## 스크롤 클릭: UI 숨기기(기본값) / 대사록 불러오기

screen preferencesScrollFunction(xa=.5, ya=.5, xo=0, yo=0):
    imagemap:
        align (xa, ya) offset (xo, yo)
        xysize (988, 666)

        auto "gui/help/%s.png"

        # Left click
        hotspot (690, 507, 299, 68) action NullAction() selected True

        # Right click
        hotspot (1, 507, 299, 65) action SetField(persistent, "rclickFunction", 0)
        hotspot (1, 572, 299, 65) action SetField(persistent, "rclickFunction", 1)

        # Scroll up
        hotspot (57, 282, 299, 65) action SetField(persistent, "scrollUpFunction", 0)
        hotspot (57, 347, 299, 65) action SetField(persistent, "scrollUpFunction", 1)

        # Scroll click
        hotspot (181, 141, 299, 65) action SetField(persistent, "scrollClickFunction", 0)
        hotspot (181, 206, 299, 65) action SetField(persistent, "scrollClickFunction", 1)

        # Scroll down
        hotspot (377,  1, 299, 65) action SetField(persistent, "scrollDownFunction", 0)
        hotspot (377, 66, 299, 65) action SetField(persistent, "scrollDownFunction", 1)

    transclude

screen preferences():

    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 화면") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                        label _("스트리밍 모드")
                        textbutton _("켜기") action SetField(persistent, "isStreaming", True)
                        textbutton _("끄기") action SetField(persistent, "isStreaming", False)

                        label _("대사 종료 표식")
                        textbutton _("표기") action SetField(persistent, "ctcDetail", True)
                        textbutton _("미표기") action SetField(persistent, "ctcDetail", False)

                    vbox:
                        style_prefix "check"
                        label _("넘기기")
                        textbutton _("읽지 않은 지문") action Preference("skip", "toggle")
                        textbutton _("선택지 이후") action Preference("after choices", "toggle")
                        textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

                ## "radio_pref" 나 "check_pref" 를 추가하여 그 외에도 환경설정
                ## 항목을 추가할 수 있습니다.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("자동 진행")

                    textbutton _("자동 진행 켜기") action Preference("auto-forward", "toggle")
                    textbutton _("클릭 후에도 자동 진행") action Preference("auto-forward after click", "toggle")

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                    label _("대사창 투명도 %d%%" % (100 - persistent.sayScreenAlpha))
                    bar value FieldValue(persistent, "sayScreenAlpha", 100) bar_invert True

                vbox:

                    if config.has_music:
                        label _("배경음 음량")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("효과음 음량")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("음성 음량")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


style preferencesScroll_text is pref_button_text:
    idle_color "#EEE"
    hover_color "#FFF"
    size 24
    yalign 1.

style preferencesScroll_button is pref_button:
    idle_background Solid("#444")
    hover_background Solid("#080")
    selected_background Solid("#400")
    selected_hover_background Solid("#440")

style preferencesScroll_vbox is pref_vbox:
    xsize 1.
    xalign .5
