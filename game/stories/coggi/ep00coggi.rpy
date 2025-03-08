default coggiProgress = 0

define coggiStories = [
    "coggiEp01Exterminator",
]

label coggiRendezvous:

    menu:
        "꼭지 스토리 진행" if coggiProgress < 1:
            call coggiStory
        "꼭지와 데이트":
            "아직 구현되지 않았습니다."

    return

label coggiStory:

    call expression coggiStories[coggiProgress]
    $ coggiProgress += 1

    return

