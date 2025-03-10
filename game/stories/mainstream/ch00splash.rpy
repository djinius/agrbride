label splashscreen:

    scene black
    if persistent.splashSettings and not splashTesting:
        pass
    else:
        call screen splashAskControl    
        call screen splashAskStreaming
        $ persistent.splashSettings = True

    call screen splashNote

    if builditTesting and not splashTesting:
        return

    if persistent.splashPlayed and not splashTesting:
        return

    if not _in_replay:
        $ persistent.myName = "나"
        $ persistent.rosalindName = "???"
    
    scene palaceGarden:
        align (.5, .5)
    with dissolve
    # 배경 – 별천지 궁전. (화려한 동양풍의 건물 내부)

    독백 "……."
    주인공 "여긴, 어디지?"
    독백 "눈이 부실 정도로 화려한 어느 궁궐."
    독백 "일상 생활에선 도저히 볼 수 없을 것만 같은, 이질적인 풍경에 나는 멍하니 주위를 둘러보았다."
    독백 "이렇게나 근사한 건물 내부를 보고 있자니 절로 기분이 들뜨기 시작했다."
    독백 "저벅저벅, 잘 포장된 돌길 위를 걸어나갔다."
    로잘린드 정면 장옷 "주인님. 그곳이 아닙니다."
    주인공 "뭐?"
    독백 "어디선가 들려오는 목소리. 나는 자동으로 그쪽을 향해 몸을 틀었다."

    # TODO:: 시녀 전원 일러스트 등장

    show 효주 정면 한복:
        pos (.70, .15) anchor (.5, .0)
        zoom .3

    show 말리 정면 한복:
        pos (.85, .15) anchor (.5, .0)
        zoom .3

    show 로잘린드 정면 장옷:
        pos (.5, 0) anchor (.5, .0)
        zoom .5
    with dissolve

    로잘린드 "이쪽입니다, 주인님."
    독백 "한 눈에 반해버릴 것만 같은 미녀가 그곳에 있었다."
    독백 "아니, 한 명이 아니었다. 나를 중심으로 하듯 둘러싼 수많은 미녀들이, 오직 나만을 바라보고 있었다."
    독백 "여자에 굶주렸던 걸까. 이런 미인들이 나오는 꿈을 다 꾸다니."
    로잘린드 "왜 그러십니까? 그렇게 빤히 제 얼굴을 보시다니."
    로잘린드 @입벌림 "혹시 어딘가 편찮으십니까?"
    독백 "조금 걱정된다는 듯, 무미건조한 표정 속에 밋밋한 변화를 준 한 명의 미녀."

    show 로잘린드 정면 보통:
        linear .75 zoom .75
    pause .75

    로잘린드 "으음. 머리에 열은 없으신 모양입니다만."
    주인공 "으앗!?"
    독백 "대뜸 나와 이마를 맞대는 미녀. 갑자기 가까워진 거리에 나는 한 번 놀랐고."
    로잘린드 "얼굴이 붉어졌군요. 체온도 조금씩 올라가고 있습니다."
    로잘린드 "설마 저 때문에 이렇게 되셨을까요?"
    독백 "너무나도 생생하게 느껴지는 부드러운 감촉에 또 한 번 당황했다."
    로잘린드 미소1 "후후. 이런 반응을 보여주시면 저도 조금 장난을 쳐보고 싶어집니다."

    ## TODO::
    # 뒷짐 지고 주인공을 올려다 보는 로잘린드 - 특수스탠딩 주문
    # 표정 - 미소, 눈 감고 입술 쭉 내밀기
    독백 "조금 짓궂은 미소를 지은 미녀가 나와 시선을 올곧게 마주쳤다."
    로잘린드 보통 "무례를 용서하시길"
    주인공 "어… 어어……?"
    독백 "그 말과 함께 눈을 감은 미녀."
    독백 "준비되지 않은 내게 미녀는 점차 입술을 가까이 댄다."
    독백 "따뜻한 숨결이 코에 닿고, 나도 그녀와 키스를……."

    $ persistent.splashPlayed = True

    return

image streamingGuide = ConditionSwitch(
    "persistent.isStreaming", "로잘린드 정면 한복",
    "True", "로잘린드 정면 몬무스")

image streamingOnOff = ConditionSwitch(
    "persistent.isStreaming", "gui/streaming/on.png",
    "True", "gui/streaming/off.png")

screen splashAskControl():
    style_prefix "splash"

    add Solid("#000")

    add "streamingGuide":
        pos (.15, .05) anchor (.5, .0)
        zoom .4

    vbox:
        pos (.3, .1) anchor (.0, .0)
        text "대사록의 특정 대사를 누르면 해당 시점으로 되돌아갈 수 있습니다."

        text "마우스 기능을 선택하십시오."
        text "게임 메뉴의 조작방법에서 바꿀 수 있습니다."
        text "UI가 사라진 상태에서 마우스 왼쪽 버튼을 클릭하면 UI가 다시 나타납니다."
        textbutton "다음" xalign .5 action Return()

    use preferencesScrollFunction(1., 1., -16, -9)

screen splashAskStreaming():
    style_prefix "splash"

    add Solid("#000")

    add "streamingGuide":
        pos (.15, .05) anchor (.5, .0)
        zoom .4

    vbox:
        pos (.3, .1) anchor (.0, .0)

        imagebutton:
            xalign .5
            action ToggleField(persistent, "isStreaming")
            auto "gui/streaming/%s.png"

        text "게임을 스트리밍 중이신가요?"

        hbox:
            xalign .5
            style_prefix "radio"
            textbutton "예" action SetField(persistent, "isStreaming", True)
            textbutton "아니요" action SetField(persistent, "isStreaming", False)

        if persistent.isStreaming:
            text "스트리밍 모드"
            text "일부 그림이 검열됩니다."

        else:
            text "일반 모드"
            text "검열되는 그림이 없습니다."

        text "모든 이야기를 감상할 수 있습니다."

        text "퀵메뉴의 {image=streamingOnOff}버튼을 눌러서 게임 도중 실시간으로 켜고 끌 수 있습니다."
        textbutton "게임 시작" xalign .5 action Return()

screen splashNote():
    frame:
        background Solid("#000")
        xysize (1., 1.)
        align (.5, .5)
    
        text "이 게임은 허구이며,\n실존하는 인물 및 기업, 종교, 단체와\n아무런 관련이 없습니다.":
            align (.5, .5)
            size 40
            color "#FFF"
            text_align .5

        at splashNoteText

    timer 3. action Return()
    key "mouseup_1" action Return()

style splash_button:
    xalign .5

style splash_text:
    align (.0, 1.)
    color "#FFF"
    xmaximum 512
    text_align .0

style splash_grid:
    xalign .5

style splash_frame:
    padding (0, 0, 0, 0)
    background None

transform splashNoteText():
    alpha .0
    linear .5 alpha 1.
    pause 1.5
    linear .5 alpha .0
