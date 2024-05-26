# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    # 도입부 1 - 로잘린드 영입
    call rosalid_01_booting
    # 도입부 2 - 나무 심고 가꾸기. 말리 영입.

    $ initBuildings()

label lobby:
    scene menubg
    로잘린드 "어서 오세요, 주인님. 오늘은 무얼 도와드릴까요?"

    menu:
        "과수원 관리":
            call buildContinue
        "데이트":
            pass
        "게임 메뉴":
            $ ShowMenu()()

    jump lobby
    return

label buildContinue:
    $ gNextLabel = None
    call screen buildit

    if gNextLabel is None:
        return
    else:
        call expression gNextLabel
        return

    return
