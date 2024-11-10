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
    scene menubg with dissolve
    로잘린드 "어서 오세요, 주인님. 오늘은 무얼 도와드릴까요?"

    menu:
        # 로잘린드
        "공부":
            pass

        # 말리, 세라, 보미, 카라
        "과수원 관리":
            call buildContinue

        # 만다
        "단련":
            pass

        # 루시, 꼭지
        "홍보":
            pass
        
        # 버스정류장
        "마실":
            scene town_mainstreet
            show 카라 몬무스:
                xalign .5 yalign .0
            with dissolve

            카라 몬무스 "오늘은 뭐하고 놀까?"

    jump lobby
    return
