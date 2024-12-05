label rosalind_bedscene:

    $ gHScene = True

    scene black
    pause 1.
    
    scene rosalind_bath:
        align (.5, .25)
    with dissolve

    로잘린드 "향상을 가로막은(閼) 것을 깨뜨려(破) 실력을 높인다(高)는 의미로 '알파고'라고 이름붙여 보았습니다."

    로잘린드 "물을 끼얹어 주십시오."
    로잘린드 "주인님과 함께 목욕하니 즐겁습니다."

    scene rosalind_bedscene:
        align (.5, .0)
    with dissolve

    로잘린드 "저를 가지세요, 주인님."

    scene rosalind_sleep:
        align (.5, .0)
    with dissolve

    독백 "피곤했는지 즐거운 시간이 끝나자 그대로 푹 잠든 로잘린드."
    독백 "나도 한숨 자 볼까."

    scene rosalind_morning:
        align (.5, .25)
    with dissolve

    로잘린드 "기침하셨습니까, 주인님?"

    scene rosalind_chinning:
        align (.5, .25)
    with dissolve

    로잘린드 "주무시는 모습이 귀엽더군요."

    scene black with dissolve

    $ gHScene = False

    return