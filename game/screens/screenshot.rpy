transform saveprogress:
    pos (20, 20) zoom 1.
    pause .5
    linear .5 pos (0, 0) zoom .0 alpha .0

screen screenshotScreen():
    zorder 200
    on "show" action FileTakeScreenshot()

    frame:
        at saveprogress
        background None
        padding (5, 5)
        add FileCurrentScreenshot(empty=None)

    timer 1.5 action Hide("screenshotScreen")
