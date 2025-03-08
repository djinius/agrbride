default mainProgress = 0

define mainStories = [
    "ch04Yutnori",
    "ch05Ramen",
    "ch06Go",
]

label mainStory:

    if mainProgress < 3:
        call expression mainStories[mainProgress]
    $ mainProgress += 1

    return




