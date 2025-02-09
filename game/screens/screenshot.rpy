transform saveprogress:
    pos (20, 20) zoom 1.
    pause .5
    linear .5 pos (0, 0) zoom .0 alpha .0

screen screenshotScreen():
    zorder 200
    on "show" action FileTakeScreenshot()

    frame at quickSaveNotify_appear:
        background Solid("#000")
        xysize (config.thumbnail_width + 10, config.thumbnail_height + 10)
        padding (5, 5)
        add FileCurrentScreenshot(empty=None)
        add "gui/help/screenshot.png" align (.0, .0) offset (5, 5)

    timer 1.25 action Hide("screenshotScreen")

## quickSaveNotify 스크린 ##################################################################
##
## Notify 스크린으로 플레이어에게 퀵세이브를 알립니다.
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen quickSaveNotify():

    zorder 100
    style_prefix "notify"

    frame at quickSaveNotify_appear:
        background Solid("#000")
        xysize (config.thumbnail_width + 10, config.thumbnail_height + 10)
        padding (5, 5)
        add FileCurrentScreenshot(empty=None)
        add "gui/help/save.png" align (.0, .0) offset (5, 5)

    timer 1.25 action Hide('quickSaveNotify')


transform quickSaveNotify_appear:
    pos (5, 5)
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0 zoom .1
