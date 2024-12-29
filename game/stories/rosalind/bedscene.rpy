label rosalind_wetdream:

    $ gHScene = True

    scene black
    pause 1.
    
    scene rosalind_bath:
        align (.5, .25)
    with dissolve

    로잘린드 "물을 끼얹어 주십시오."
    로잘린드 "주인님과 함께 목욕하니 즐겁습니다."
    로잘린드 "왜 그러십니까? 제게서 눈을 떼지 못하시는군요."

    $ gHScene = True

    show white
    pause .5
    hide white
    pause .5
    show white
    pause .25
    hide white
    pause .25

    $ loop = 5

    while loop > 0:
        show white
        pause .1
        hide white
        pause .1
        $ loop -= 1

    scene black with Dissolve(2.)
    pause 1.

    $ gHScene = False

    독백 "으, 찝찝해. 설마......"
    독백 "이런 데서 몽정을 다 하다니."

    scene black with dissolve

    return


label rosalind_bedscene:

    $ gHScene = True

    scene black
    pause 1.
    
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