default rosalindProgress = 0
default rosalindDenied = False

define rosalindStories = [
    "rosalindEp01HumanComputer",
    "rosalindEp02Programming",
    "rosalindEp03_0WetDream",
    "rosalindEp04Fear",
    "rosalindEp05Princess"
]

label rosalindRendezvous:

    menu:
        "로잘린드 스토리 진행" if rosalindProgress < 5:
            call rosalindStory
        "로잘린드와 데이트":
            "아직 구현되지 않았습니다."

    return

label rosalindStory:

    if (rosalindProgress == 3) and (rosalindDenied is True):
        call rosalindEp03_1Apologize
        $ rosalindDeined = False
    else:
        call expression rosalindStories[rosalindProgress]

    $ rosalindProgress += 1

    return