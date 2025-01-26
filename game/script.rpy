# 이 파일에 게임 스크립트를 입력합니다.

default builditTesting = True
default _in_gameplay = False

# 여기에서부터 게임이 시작합니다.
label start:
    $ rosalindName = "로잘린드"
    $ _in_gameplay = True

    # call ch01Opening from _call_ch01Opening
    # call ch02Tutor
    # call ch03Eclosion
    # call rosalindWetDream
    # call rosalindHappyEnding
    call maliHappyEnding

    return

    $ initBuildings()

    scene black

    call lobby from _call_lobby

label buildContinue:
    call screen buildit

    if nextCutScene is not None:
        call playCutScene(nextCutScene) from _call_playCutScene
        jump buildContinue

    return
