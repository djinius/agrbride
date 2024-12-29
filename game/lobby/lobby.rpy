screen lobbyMenu(items):

    use choice(items)

    text "나들이: %d/%d" % (gDates, getIdlePopulation() // 1000) align (.0, .0) color "#FFF"

label lobby:
    scene black:
        align (.5, .25)
    with dissolve

    로잘린드 정면 "어서 오세요, 주인님. 오늘은 무얼 도와드릴까요?"

    $ rosalindName = "로잘린드"

    menu(screen = "lobbyMenu"):
        # 말리, 세라, 보미, 카라
        "영지 관리":
            call buildContinue from _call_buildContinue

        # 버스정류장
        "나들이" if isDateAvailable():
            call rosalind_bedscene from _call_rosalind_bedscene
            $ gDates += 1

        "스토리 진행" if isDateAvailable():
            call rosalind_wetdream from _call_rosalind_wetdream
            $ gDates += 1
            $ addExperience()

    jump lobby
    return
