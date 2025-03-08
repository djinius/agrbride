default gIsEndingEnabled = False

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
        "영지 관리"(noHistory=True):
            call buildContinue

        "스토리 진행" if isStoryAvailable() and mainProgress < len(mainStories):
            call mainStory
            $ gDates += 1
            $ addExperience()

        "로잘린드" if isDateAvailable() and rosalindProgress < len(rosalindStories):
            call rosalindRendezvous
            $ gDates += 1

        "말리" if isDateAvailable() and maliProgress < len(maliStories):
            call maliRendezvous
            $ gDates += 1

        "루시" if isDateAvailable() and lucyProgress < len(lucyStories):
            call lucyRendezvous
            $ gDates += 1

        "꼭지" if isDateAvailable() and coggiProgress < len(coggiStories):
            call coggiRendezvous
            $ gDates += 1

        "카라" if isDateAvailable() and charaProgress < len(charaStories):
            call charaRendezvous
            $ gDates += 1

        "효주" if isDateAvailable() and hyojuProgress < len(hyojuStories):
            call hyojuRendezvous
            $ gDates += 1

        "엔딩" if isDateAvailable() and mainProgress >= len(mainStories):
            $ gIsEndingEnabled = True
            return

    jump lobby
    return
