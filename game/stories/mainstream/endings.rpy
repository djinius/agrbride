label endingBegin(forcePlay = False):

    if builditTesting and (not forcePlay):
        return

    수나 "연산회로 42억 9496만 7296개를 병렬 연결해 후작이 돌아갈 시공간 좌표를 특정할 수 있었도다."
    수나 "내 우화가 임박했노라. 우화한 이후라면 내 마력도 충분히 성장할 것이니라. 그럼 돌려보내 줄 수 있도다."
    수나 "7일만 기다리거라."

    "(7일 후 성인 모습으로 나타난 수나.)"
    수나 "후작. 별천지에서 원하는 것이 있느냐?"
    수나 "감사의 표시로 후작이 원하는 것을 하사하겠노라."

    menu:
        "노멀 엔딩":
            call normalEnding(forcePlay)
        "로잘린드 엔딩":
            call rosalindHappyEnding(forcePlay)
        "말리 엔딩":
            call maliHappyEnding(forcePlay)
        "트루 엔딩":
            call trueEnding(forcePlay)

    return


label normalEnding(forcePlay = False):

    if builditTesting and (not forcePlay):
        return

    주인공 "아니. 그간 함께 했던 추억만으로도 충분해."
    수나 "그간 고마웠느니라, 후작. 잘 가거라."

    독백 "별천지로 올 때처럼 거대한 힘이 내 몸을 끌어당긴다."
    독백 "눈을 떠 보니 내 자취방 앞이었다. 문도 그대로 열려 있었다."
    독백 "이크. 지금 바로 나가지 않으면 지각하겠다. 즉시 학교로 뛰었다."

    scene college with dissolve

    독백 "수업이 끝났다."
    독백 "별천지에서 있었던 일이 꿈만 같다. 아니, 정말 꿈이었나?"
    독백 "하룻밤의 꿈은 묻어버리고 내 앞날 준비에 충실해야겠지."
    독백 "오늘도 또 과제다. 집으로 돌아가 볼까나……."
    "(엔딩 크레딧)"

    return
