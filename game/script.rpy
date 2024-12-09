# 이 파일에 게임 스크립트를 입력합니다.

# 여기에서부터 게임이 시작합니다.
label start:
    $ rosalindName = "로잘린드"
    call opening

    $ initBuildings()

    scene black

    # $ helloworld = renpy.input(screen='koreaninput', prompt='뭐든지 입력하세요')
    # 카라 "[helloworld]"

    call lobby

label buildContinue:
    call screen buildit

    if nextCutScene is not None:
        call playCutScene(nextCutScene)
        jump buildContinue

    return
