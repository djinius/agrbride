screen lobbyMenu(items):
    default spirits = ["로잘린드", "말리", "만다", "꼭지", "루시"]
    default actionIndex = [0, 1, 2, 3, 3]
    default positions = [(.9, .9), (.1, .9), (.1, .7), (.2, .5), (.3, .5)]

    for n, i in enumerate(actionIndex):
        imagebutton:
            idle spirits[n] + " 로비"
            action items[i].action
            pos positions[n] anchor (.5, .5)
            focus_mask True


label lobby:
    scene menubg:
        align (.5, .25)
    with dissolve

    로잘린드 정면 "어서 오세요, 주인님. 오늘은 무얼 도와드릴까요?"

    $ rosalindName = "로잘린드"

    menu:
        # 말리, 세라, 보미, 카라
        "과수원 관리":
            call buildContinue

        # 버스정류장
        "마실":
            call rosalind_bedscene

    jump lobby
    return
