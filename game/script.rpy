# 이 파일에 게임 스크립트를 입력합니다.

# 여기에서부터 게임이 시작합니다.
label start:

    scene black

    show well:
        align (.2, .5)

    show appleTree3:
        align (.4, .5)

    show grapeTree3:
        align (.6, .5)

    show peachTree3:
        align (.8, .5)

    카라 "아싸"
    말리 "콩팥"
    로잘린드 "하하하하"

    $ initBuildings()

    call lobby

label buildContinue:
    call screen buildit

    if nextCutScene is not None:
        call playCutScene(nextCutScene)

    return
