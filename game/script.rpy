# 이 파일에 게임 스크립트를 입력합니다.

default builditTesting = False
default _in_gameplay = False

# 여기에서부터 게임이 시작합니다.
label start:
    $ persistent.rosalindName = "로잘린드"
    $ _in_gameplay = True

    call ch01Opening
    call ch02Tutor
    call ch03Eclosion
    call rosalindEp01HumanComputer(True)
    call rosalindEp03WetDream(True)

    call endingBegin(True)
    return

    $ initBuildings()

    scene black

    call lobby

label buildContinue:
    call screen buildit

    if nextCutScene is not None:
        call playCutScene(nextCutScene)
        jump buildContinue

    return
