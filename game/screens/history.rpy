## History 스크린 #################################################################
##
## 지난 대사록을 출력합니다. _history_list 에 저장된 대사 기록을 확인합니다.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 이 스크린은 내용이 아주 많을 수 있으므로 prediction을 끕니다.
    predict False

    use game_menu(_("대사록"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            button:
                action Confirm("이 장면으로 되돌아가시겠습니까?", RollbackToIdentifier(h.rollback_identifier))
                sensitive (_in_gameplay) and (renpy.get_identifier_checkpoints(h.rollback_identifier))

                has frame

                ## history_height 이 None일 경우 레이아웃이 틀어지지 않게 합니
                ## 다.

                if isinstance(h, HistoryMenuEntry):
                    style "history_menu_frame"

                    grid 1 len(h.items):
                        align (.5, .5)
                        for mi in h.items.keys():
                            text mi:
                                xalign .5
                                text_align .5
                                if h.items[mi]:
                                    color "#FFFF00"
                                else:
                                    color "#FFFFFF"

                else:
                    fixed:
                        yfit True
                        if h.who:

                            label h.who:
                                style "history_name"
                                substitute False

                                ## 화자 Character에 화자 색깔이 지정되어 있으면 불러옵니
                                ## 다.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False
                            color "#FFF"

        if not _history_list:
            label _("대사가 없습니다.")


## 이것은 대사록 화면에 표시할 수 있는 태그를 결정합니다.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_button:
    xfill True
    ysize gui.history_height

style history_frame:
    xfill True
    ysize gui.history_height
    insensitive_background "#8888"
    idle_background "#0000"
    hover_background "#008F"

style history_menu_frame:
    xfill True
    yminimum 192
    insensitive_background "#8888"
    idle_background "#00008888"
    hover_background "#0000CCCC"

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    color "#FFF"
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


