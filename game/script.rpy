﻿# 이 파일에 게임 스크립트를 입력합니다.

default builditTesting = True
default _in_gameplay = False

# 여기에서부터 게임이 시작합니다.
label start:
    $ persistent.rosalindName = "로잘린드"
    $ _in_gameplay = True

    call ch01Opening
    call ch02Tutor
    call ch03Eclosion
    call rosalindEp01HumanComputer
    call rosalindEp03_0WetDream
    call rosalindEp03_1Apologize
    call rosalindEp06Trauma
    call hyojuEpFirstSex
    call charaEp01Discourtesy(True)

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
