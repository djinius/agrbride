default lucyProgress = 0

define lucyStories = [
    "lucyEp01LampPost",
]

label lucyRendezvous:

    menu:
        "루시 스토리 진행" if lucyProgress < 1:
            call lucyStory
        "루시와 데이트":
            "아직 구현되지 않았습니다."

    return

label lucyStory:

    call expression lucyStories[lucyProgress]
    $ lucyProgress += 1

    return

