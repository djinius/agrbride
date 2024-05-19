# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    call rosalid_01_booting

    $ initBuildings()

label buildContinue:
    $ gNextLabel = None
    call screen buildit

    if gNextLabel is None:
        jump buildContinue
    else:
        call expression gNextLabel
        jump buildContinue

    return

label gameMenu:
    scene menubg
    로잘린드 "어서 오세요, 주인님. 오늘은 무얼 도와드릴까요?"
    $ ShowMenu()()
    로잘린드 "도움이 필요하면 언제든 찾아오세요."

    return