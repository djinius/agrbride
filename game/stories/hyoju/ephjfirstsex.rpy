label hyojuEpFirstSex(forcePlay = False):

    if builditTesting and (not forcePlay):
        return

    독백 "효주는 내 몸을 침대 위에 집어던졌다."
    주인공 "야. 너무 난폭하잖아?"
    효주 "그 정도로는 끄떡도 없으면서 엄살 부릴래?"
    주인공 "그래도 분위기라는 게 있지."
    효주 "어허! 시원시원하게 가자고."
    독백 "효주가 손을 휘젓자 내 옷이 모두 벗겨졌다."
    독백 "뭔가 남녀가 바뀐 느낌인데?"
    효주 "훗! 그럼……."

    "(철푸덕!)"
    독백 "효주는 옷도 벗지 않고 내 위에 올라탔다. 내 분신이 그대로 꽂혀 들어갔다."
    효주 "허… 허헉……."
    효주 "어… 어이없다. 이거… 아프네."
    주인공 "다짜고짜 대드니까 그렇지."
    효주 "에잉 몰라. 기왕 시작한 거 끝을 보자고."

    독백 "한바탕 뜨거운 사랑을 나누었다."

    # 침대에 누운 효주

    scene hyoju_bed with dissolve
    $ gHScene = True

    효주 "이것도 운동이 꽤 되는군."
    주인공 "지구에서는 이걸로 살 빼는 사람들도 있었으니까."
    효주 "또 할래?"
    주인공 "그러려면 시간이 좀 걸려."
    효주 "흠. 그래? 잠깐……."
    독백 "효주는 무언가를 먹듯 오물거리더니 내게 입을 맞추었다."
    "(꼴깍꼴깍)"
    독백 "미지근하고 달착지근한 액체가 내 입으로 넘어온다."
    주인공 "푸하……."
    주인공 "이게 뭐야?"
    효주 "영양교환이야. 내 특기지."
    효주 "기운이 빠졌을 때 도움이 될 거야."
    주인공 "도움이 되는 정도가 아닌데?"
    독백 "막 자고 일어난 듯 온몸에 활력이 돈다."
    독백 "누워 있는 효주의 위로 올라갔다."
    효주 "이번엔 후작이 이끌어 줘."

    # 애무 H신 메뉴 구현

    독백 "우리는 체력이 다 할 때까지 사랑을 나누었다."
    효주 "이젠 손끝 하나 까딱 못 하겠어."
    주인공 "나 역시."
    효주 "이대로 함께 잠들자."
    주인공 "그래. 팔베개 해 줄까?"
    효주 "후후……."
    효주 "나보다 강한 누군가에게 안겨 있는 느낌이 이렇구나. 포근하고 듬직해서 좋아."
    효주 "잘 자, 후작."
    주인공 "잘 자, 효주."

    $ gHScene = False
    scene black with dissolve

    return
