define fadeoutin = Fade(.5, .0, .5, color="#000")

label ejaculate:
    show white with Dissolve(.5)
    hide white with Dissolve(.25)
    show white with Dissolve(.125)
    hide white with Dissolve(.125)

    $ loop = 5

    while loop > 0:
        show white with Dissolve(.075)
        hide white with Dissolve(.075)
        $ loop -= 1

    return

