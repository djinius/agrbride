define fadeoutin = Fade(.5, .0, .5, color="#000")

label ejaculate:
    show white
    pause .5
    hide white
    pause .25
    show white
    pause .125
    hide white
    pause .125

    $ loop = 5

    while loop > 0:
        show white
        pause .075
        hide white
        pause .075
        $ loop -= 1

    return

