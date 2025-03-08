default charaProgress = 0

define charaStories = [
    "charaEp01Discourtesy",
]

label charaRendezvous:

    menu:
        "카라 스토리 진행" if charaProgress < 1:
            call charaStory
        "카라와 데이트":
            "아직 구현되지 않았습니다."

    return

label charaStory:

    call expression charaStories[charaProgress]
    $ charaProgress += 1

    return

