default cutscenes = [
    RosalindAppleTreeScene(),
    RosalindOneAppleTreeScene(),
    RosalindFactoryScene(),
    RosalindWellScene(),
    RosalindUpgradeScene(),
    MaliSharonScene(),
    RosalindDateScene()
    ]

label playCutScene(cutSceneObject):

    $ gShowPopupMenu = False
    $ gShowDetails = None
    $ gTargetTree = None
    $ xLoc = None
    $ yLoc = None

    show screen buildit(isManageEnabled = False)

    call expression cutSceneObject.getLabelName()
    $ cutSceneObject.finish()
    $ nextCutScene = None

    # hide screen buildit

    return

label rosalindAppleTreeScene:

    로잘린드 몬무스 "식량을 확보해야 영민들을 불러모을 수 있습니다."
    로잘린드 "빈 땅을 선택하면 어떤 작물을 심을 수 있는지 확인이 가능합니다."
    로잘린드 "사과나무는 가장 기본이 되는 식량수입니다."
    로잘린드 "빈 땅을 선택해 사과나무를 심어 보십시오."
    로잘린드 "말리 님께서 땅속줄기를 뻗어 새로운 나무를 생성해 주실 겁니다."

    return

label rosalindOneAppleTreeScene:

    로잘린드 몬무스 "잘하셨습니다. 영지에 인구가 유입되고 있군요."
    로잘린드 "사과나무를 한 그루 더 심어 보십시오."

    return

label rosalindFactoryScene:

    로잘린드 "공방을 설치할 때가 되었습니다."
    로잘린드 "목재를 수확해서 영지에서 사용할 각종 기물을 만드는 곳입니다."
    로잘린드 "말리 님의 줄기 중 오래 되거나 웃자란 가지들을 베어내 활용합니다."
    로잘린드 "목재 일부를 활용해서 식량수의 등급을 올릴 수도 있습니다."

    return

label rosalindWellScene:

    로잘린드 몬무스 "영지에 나무가 계속 늘어나고 있군요. 아주 좋습니다."
    로잘린드 "그만큼 물도 많이 필요해집니다."
    로잘린드 "우물을 파서 수자원을 확보해 보십시오. 버드나무도 우물 옆에 함께 심어서 깨끗한 물을 얻어야 합니다."
    로잘린드 "영민들도 물을 소비하기 때문에, 식량수에서 필요로 하는 양보다 더 많은 수자원을 넉넉히 준비해 두어야 합니다."

    return

label rosalindUpgradeScene:

    로잘린드 몬무스 "목재가 필요한만큼 모였습니다."
    로잘린드 "사과나무 한 그루를 골라서 등급을 향상시켜 보십시오."
    로잘린드 "인구와 목재 생산량이 늘어납니다. 그만큼 물 수요량도 늘어나지요."

    return

label maliSharonScene:

    말리 몬무스 "오, 이런 자기."
    말리 "내 열매를 노리고 해충들이 몰려들고 있어."
    말리 "무궁화나무를 심어. 해충들을 소탕할 전초기지가 되어 줄 거야."

    return

label rosalindDateScene:

    로잘린드 몬무스 "이제 한숨 돌릴 수 있겠군요."
    로잘린드 "대기 인력이 1,000명을 넘을 때마다 한 번씩 숨을 돌릴 기회가 찾아옵니다."
    로잘린드 "그러면 휴식을 취하거나, 가까운 곳으로 나들이를 갈 수도 있겠지요."

    return

label rosalindFactoryUpgradeScene:

    로잘린드 몬무스 "공방의 등급을 올릴 수 있습니다."
    로잘린드 "목재의 보관량이 늘어나고 새로운 물건을 생산할 수 있게 됩니다."
    로잘린드 "새로이 생산되는 물건은 식량수 등급을 올리는 데 사용됩니다."

    return

