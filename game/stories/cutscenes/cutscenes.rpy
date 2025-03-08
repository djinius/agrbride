default cutscenes = [
    RosalindAppleTreeScene(),
    RosalindResidenceScene(),
    RosalindFactoryScene(),
    MaliWellScene(),
    RosalindUpgradeScene(),
    CoggiSharonScene(),
    RosalindDateScene(),
    RosalindFactoryUpgradeScene(),
    ]

label playCutScene(cutSceneObject):

    $ gShowPopupMenu = False
    $ gShowDetails = None
    $ gTargetTree = None
    $ xLoc = None
    $ yLoc = None

    $ cutSceneObject.begin()

    show screen buildit(isManageEnabled = False)

    call expression cutSceneObject.getLabelName()
    $ cutSceneObject.finish()
    $ nextCutScene = None

    # hide screen buildit

    return

label rosalindAppleTreeScene:

    로잘린드 정면 예복 "로잘린드, 다시 인사드립니다."
    로잘린드 "주인님께 영지 관리 업무를 안내드리려 합니다."
    로잘린드 "영지의 기반은 영민입니다. 영민이 많을수록 영지의 힘이 강해지고, 공주님께서 낳으실 알들도 충실히 돌볼 수 있습니다."
    로잘린드 "영민들을 모으려면 우선 식량을 제공하는 식량수를 심어야 합니다."
    로잘린드 미소1 "지금은 맨 처음이기에 가장 기본이 되는 사과나무를 심을 수 있습니다."
    로잘린드 보통 "빈 땅을 선택해 사과나무를 심어 보십시오."
    로잘린드 "말리 님께서 땅속줄기를 뻗어 새로운 나무를 생성해 주실 겁니다."

    return

label rosalindResidenceScene:

    로잘린드 정면 예복 미소2 "잘하셨습니다."
    로잘린드 보통 "모든 나무와 건물은 정해진 만큼의 관리 인력을 필요로 합니다."
    로잘린드 "지금은 인구가 우리 여덟 명 뿐입니다. 식량수를 관리할 영민들을 불러모을 차례입니다."
    로잘린드 "관리 인력보다 현재 영민들이 적다면 새로운 식량수를 건설할 수 없습니다."
    로잘린드 "또한 영지의 총 인구는 식량 공급을 넘을 수 없습니다."
    로잘린드 "영민들이 머무를 숙소를 마련해 볼까요? 빈 땅을 선택해 거주구를 건설해 보십시오."
    로잘린드 "거주구 근처의 식량수는 식량 수확량이 늘어납니다. 이 점을 감안해 거주구를 배치하는 게 좋습니다."

    return

label rosalindUpgradeScene:

    로잘린드 정면 예복 미소1 "잘하셨습니다."
    로잘린드 보통 "대부분의 건물은 등급을 올려서 수용 인원을 증가시키거나 생산량을 증대시킬 수 있습니다."
    로잘린드 "거주구의 등급을 향상시켜 보십시오. 거주구 옆에 있는 말풍선을 누르거나, 오른쪽 클릭 후 '등급 향상'을 선택하면 됩니다."
    로잘린드 "인구가 늘어나며, 그만큼 물 수요량도 늘어나지요."

    return

label rosalindFactoryScene:

    로잘린드 정면 예복 미소1 "영지 등급이 한 단계 올라갔습니다."
    로잘린드 미소2 "건물을 짓거나 나무를 심고 등급을 올릴 때마다 영지에 경험치가 쌓입니다."
    로잘린드 미소1 "경험치가 일정량 쌓일 때마다 영지의 등급이 올라갑니다."
    로잘린드 보통 "이제부터 공방을 사용할 수 있습니다."
    로잘린드 @입벌림 "영지에서 사용할 각종 기물을 만드는 곳입니다."
    로잘린드 "공방에서 만드는 기물을 활용해서 나무와 건물의 등급을 올릴 수 있으며,\n다른 영지에 팔아서 금편을 벌 수도 있습니다."

    return

label maliWellScene:

    말리 정면 몬무스 "오, 이런 자기."
    말리 "영민과 나무가 계속 늘어나는 건 좋지만 물도 그만큼 더 필요해."
    말리 "우물을 파서 수자원을 확보해야 해."
    말리 "버드나무를 심으면 내가 수기를 감지해서 지하수를 끌어올려 줄게."
    말리 "우물 근처에서는 식량 생산이 늘어나니까 참고하도록 해."

    return

label hyojuStatiumScene:

    효주 "요. 열심히 하는데?"
    효주 "영민들이 뛰어놀 공간을 만들어 줘."
    효주 "열심히 체력을 단련하면 식량 수확량도 늘어나고, 운동장에서 놀 영민들도 더 많이 영입될 거야."

    return

label coggiSharonScene:

    꼭지 "열심히 하네, 오빠. 결과도 좋아."
    꼭지 "말리가 만드는 열매에 해충들이 몰려들고 있어."
    꼭지 "무궁화나무를 심어. 해충들을 유인해 줄 거야."
    꼭지 "무궁화 주변에서는 수확량이 3할 늘어나니까 배치에 신경써 봐."

    return

label rosalindDateScene:

    로잘린드 정면 "이제 한숨 돌릴 수 있겠군요."
    로잘린드 "대기 인력이 1,000명을 넘을 때마다 한 번씩 숨을 돌릴 기회가 찾아옵니다."
    로잘린드 "그러면 휴식을 취하거나, 가까운 곳으로 나들이를 갈 수도 있겠지요."

    return

label rosalindFactoryUpgradeScene:

    로잘린드 정면 "공방의 등급을 올릴 수 있습니다."
    로잘린드 "공방의 등급이 올라갈수록 더욱 많은 기물을 생산할 수 있게 됩니다."
    로잘린드 "새로이 생산되는 물건은 식량수 등급을 올리는 데 사용됩니다."

    return

