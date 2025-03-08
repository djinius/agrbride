default hyojuProgress = 0

define hyojuStories = [
    "hyojuEp01Exercise",
]

label hyojuRendezvous:

    menu:
        "효주 스토리 진행" if hyojuProgress < 1:
            call hyojuStory
        "효주와 데이트":
            "아직 구현되지 않았습니다."

    return

label hyojuStory:

    call expression hyojuStories[hyojuProgress]
    $ hyojuProgress += 1

    return

