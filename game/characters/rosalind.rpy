default persistent.rosalindName = "???"
default rosalindHappyTime = False
default rosalindHSceneEnabled = False

define 로잘린드 = Character('persistent.rosalindName', dynamic=True, color="#B1DFD0", image="로잘린드", ctc="ctc35Blink", ctc_position="nestled-close", screen='sayRosalind')

screen sayRosalind(who, what):
    use sayCommon(who, what, hcolor="#214F40")

# 정면
# 얼굴 표정요소 좌표: (976, 359)
# 눈썹: 1332,327
# 눈: 1313, 378
# 입: 1328, 518
# 더듬이: 1097, 0

layeredimage 로잘린드:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/rosalind/body/wing.png"

    group body:
        attribute 작업복 default:
            "images/characters/rosalind/body/smock.png"
        attribute 일상복1:
            "images/characters/rosalind/body/comfort.png"
        attribute 일상복2:
            "images/characters/rosalind/body/sexy.png"
        attribute 한복:
            "images/characters/rosalind/body/hanbok.png"
        attribute 장옷:
            "images/characters/rosalind/body/hanbok_coat.png"
        attribute 누드:
            ConditionSwitch("persistent.isStreaming", "images/characters/rosalind/body/nude_censored.png",
                            "True", "images/characters/rosalind/body/nude.png")
        attribute 예복:
            ConditionSwitch("rosalindHappyTime", "images/characters/rosalind/body/hanbok_coat.png",
                            "True", "images/characters/rosalind/body/hanbok.png")
        attribute 일상복:
            ConditionSwitch("rosalindHSceneEnabled", "images/characters/rosalind/body/comfort.png",
                            "True", "images/characters/rosalind/body/sexy.png")

    group antenna:
        pos (1097, 0)
        attribute 더듬이_보통 default:
            "images/characters/rosalind/antennae/dark.png"
        attribute 더듬이_빛남:
            "images/characters/rosalind/antennae/glowing.png"
        attribute 더듬이_없음:
            Null()

    group eyebrows:
        pos (1332, 327)
        attribute 눈썹_보통 default:
            "images/characters/rosalind/eyebrows/normal.png"
        attribute 눈썹_웃음:
            "images/characters/rosalind/eyebrows/smile.png"
        attribute 눈썹_놀람:
            "images/characters/rosalind/eyebrows/surprised.png"
        attribute 눈썹_풀죽음:
            "images/characters/rosalind/eyebrows/timid.png"
        attribute 눈썹_분노:
            "images/characters/rosalind/eyebrows/angry.png"

    group eyes:
        pos (1313, 378)
        attribute 눈_보통 default:
            "images/characters/rosalind/eyes/normal.png"
        attribute 눈_황당:
            "images/characters/rosalind/eyes/absurd.png"
        attribute 눈_분노:
            "images/characters/rosalind/eyes/angry.png"
        attribute 눈_외면:
            "images/characters/rosalind/eyes/away.png"
        attribute 눈_감음:
            "images/characters/rosalind/eyes/closed.png"
        attribute 눈_하트:
            "images/characters/rosalind/eyes/hearteyes.png"
        attribute 눈_실눈:
            "images/characters/rosalind/eyes/laugh_halfopen.png"
        attribute 눈_웃음:
            "images/characters/rosalind/eyes/smile_closed.png"
        attribute 눈_놀람:
            "images/characters/rosalind/eyes/surprised.png"
        attribute 눈_윙크:
            "images/characters/rosalind/eyes/wink.png"

    group mouth:
        pos (1328, 518)
        attribute 입_보통 default:
            "images/characters/rosalind/mouth/normal.png"
        attribute 입_황당:
            "images/characters/rosalind/mouth/absurd.png"
        attribute 입_메롱:
            "images/characters/rosalind/mouth/boo.png"
        attribute 입_키스:
            "images/characters/rosalind/mouth/kiss.png"
        attribute 입_폭소:
            "images/characters/rosalind/mouth/laugh.png"
        attribute 입_크게벌림:
            "images/characters/rosalind/mouth/open_large.png"
        attribute 입_벌림:
            "images/characters/rosalind/mouth/open_small.png"
        attribute 입_우쭐:
            "images/characters/rosalind/mouth/proud.png"
        attribute 입_미소:
            "images/characters/rosalind/mouth/smile_closed.png"
        attribute 입_미소벌림:
            "images/characters/rosalind/mouth/smile_halfopen.png"
        attribute 입_미소치아:
            "images/characters/rosalind/mouth/smile_teeth.png"
        attribute 입_삐침:
            "images/characters/rosalind/mouth/sulk.png"
        attribute 입_혀내밂:
            "images/characters/rosalind/mouth/tongue.png"

image side 로잘린드 = LayeredImageProxy("로잘린드", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

layeredimage 로잘린드 유년기:
    group whole:
        attribute 보통 default:
            "images/characters/rosalind/youth/normal.png"
        attribute 입벌림:
            "images/characters/rosalind/youth/speak.png"
        attribute 미소:
            "images/characters/rosalind/youth/smile.png"
        attribute 분노:
            "images/characters/rosalind/youth/angry.png"

image side 로잘린드 유년기 = LayeredImageProxy("로잘린드 유년기", Transform(crop=(150, 0, 1100, 1500), zoom=.4))

