default maliProgress = 0

define maliStories = [
    "maliEp01ThanksGiving",
]

label maliRendezvous:

    menu:
        "말리 스토리 진행" if maliProgress < 1:
            call maliStory
        "말리와 데이트":
            "아직 구현되지 않았습니다."

    return

label maliStory:

    call expression maliStories[maliProgress]
    $ maliProgress += 1

    return

