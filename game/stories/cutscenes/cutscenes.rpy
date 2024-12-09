default cutscenes = [
    RosalindAppleTreeScene(),
    RosalindOneAppleTreeScene(),
    RosalindFactoryScene(),
    RosalindWellScene(),
    RosalindUpgradeScene(),
    MaliSharonScene(),
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

    로잘린드 정면 몬무스 "로잘린드, 다시 인사드립니다."
    로잘린드 "영지에 신문물을 보급하려면, 영지가 어떻게 운영되는지 아셔야 합니다."
    로잘린드 "수석 시녀인 제가 하나하나 함께 하며 알려드리겠습니다."
    로잘린드 "영지의 기반은 영민입니다. 영민이 많을수록 영지의 힘이 강해지고, 공주님께서 낳으실 알들도 충실히 돌볼 수 있습니다."
    로잘린드 "영민들을 모으려면 우선 식량을 제공하는 식량수를 심어야 합니다."
    로잘린드 "지금은 맨 처음이기에 가장 기본이 되는 사과나무를 심을 수 있습니다."
    로잘린드 "빈 땅을 선택해 사과나무를 심어 보십시오."
    로잘린드 "말리 님께서 땅속줄기를 뻗어 새로운 나무를 생성해 주실 겁니다."

    return

label rosalindOneAppleTreeScene:

    로잘린드 정면 몬무스 미소2 "잘하셨습니다. 영민들이 유입되고 있군요."
    로잘린드 보통 "사과나무를 한 그루 더 심어 보십시오."

    return

label rosalindFactoryScene:

    로잘린드 정면 몬무스 미소1 "이제부터 공방을 사용할 수 있습니다."
    로잘린드 보통 "목재를 수확해서 영지에서 사용할 각종 기물을 만드는 곳입니다."
    로잘린드 "말리 님의 줄기 중 오래 되거나 웃자란 가지들을 베어내 활용합니다."
    로잘린드 "공방에서 만드는 기물을 활용해서 식량수의 등급을 올릴 수도 있습니다."
    로잘린드 "목재는 자동으로 수확되며, 다른 기물은 직접 제작 지시를 내려야 합니다."

    return

label rosalindWellScene:

    로잘린드 몬무스 정면 미소2 "영지에 나무와 인구가 계속 늘어나고 있군요. 아주 좋습니다."
    로잘린드 "그만큼 물도 많이 필요해집니다."
    로잘린드 "우물을 파서 수자원을 확보해 보십시오. 버드나무도 우물 옆에 함께 심어서 깨끗한 물을 얻어야 합니다."
    로잘린드 "영민들도 물을 소비하기 때문에, 식량수에서 필요로 하는 양보다 더 많은 수자원을 넉넉히 준비해 두어야 합니다."
    로잘린드 "또한, 우물 근처에 위치한 식량수는 소출이 3할 늘어납니다."

    return

label rosalindUpgradeScene:

    로잘린드 몬무스 정면 "목재가 필요한만큼 모였습니다."
    로잘린드 "사과나무 한 그루를 골라서 등급을 향상시켜 보십시오."
    로잘린드 "인구와 목재 생산량이 늘어납니다. 그만큼 물 수요량도 늘어나지요."

    return

label maliSharonScene:

    말리 몬무스 "오, 이런 자기."
    말리 "내 열매를 노리고 해충들이 몰려들고 있어."
    말리 "무궁화나무를 심어. 해충들을 소탕할 전초기지가 되어 줄 거야."
    말리 "무궁화나무가 없는 곳에서는 생산량이 3할 줄어들어."

    return

label rosalindDateScene:

    로잘린드 정면 "이제 한숨 돌릴 수 있겠군요."
    로잘린드 "대기 인력이 1,000명을 넘을 때마다 한 번씩 숨을 돌릴 기회가 찾아옵니다."
    로잘린드 "그러면 휴식을 취하거나, 가까운 곳으로 나들이를 갈 수도 있겠지요."

    return

label rosalindFactoryUpgradeScene:

    로잘린드 정면 "공방의 등급을 올릴 수 있습니다."
    로잘린드 "목재의 보관량이 늘어나고 새로운 물건을 생산할 수 있게 됩니다."
    로잘린드 "새로이 생산되는 물건은 식량수 등급을 올리는 데 사용됩니다."

    return

