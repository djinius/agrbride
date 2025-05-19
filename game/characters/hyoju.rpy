# 앞머리: (724, 0)
# 눈썹: (1128, 286)
# 눈: (1114, 216)
# 입: (1184, 463)

define 효주 = Character('효주', color="#FFE600", image="효주", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayHyoju")
default hyojuHSceneEnabled = False

screen sayHyoju(who, what):
    use sayCommon(who, what, hcolor="#8F7600")

layeredimage 효주:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/hyoju/body/wing.png"

    group body:
        attribute 작업복 default:
            ConditionSwitch("persistent.isStreaming", "images/characters/hyoju/body/smock_censored.png",
                            "True", "images/characters/hyoju/body/smock.png")
        attribute 일상복1:
            "images/characters/hyoju/body/comfort.png"
        attribute 일상복2:
            ConditionSwitch("persistent.isStreaming", "images/characters/hyoju/body/sexy_censored.png",
                            "True", "images/characters/hyoju/body/sexy.png")
        attribute 한복:
            "images/characters/hyoju/body/hanbok.png"
        attribute 누드:
            ConditionSwitch("persistent.isStreaming", "images/characters/hyoju/body/nude_censored.png",
                            "True", "images/characters/hyoju/body/nude.png")
        attribute 예복:
            "images/characters/hyoju/body/hanbok.png"
        attribute 일상복:
            ConditionSwitch("hyojuHSceneEnabled", "images/characters/hyoju/body/comfort.png",
                            "True", "images/characters/hyoju/body/sexy.png")

    group eyebrows:
        pos (1128, 286)
        attribute 눈썹_보통 default:
            "images/characters/hyoju/eyebrows/normal.png"
        attribute 눈썹_웃음:
            "images/characters/hyoju/eyebrows/smile.png"
        attribute 눈썹_놀람:
            "images/characters/hyoju/eyebrows/surprised.png"
        attribute 눈썹_풀죽음:
            "images/characters/hyoju/eyebrows/timid.png"
        attribute 눈썹_분노:
            "images/characters/hyoju/eyebrows/angry.png"

    group eyes:
        pos (1114, 216)
        attribute 눈_보통 default:
            "images/characters/hyoju/eyes/normal.png"
        attribute 눈_황당:
            "images/characters/hyoju/eyes/absurd.png"
        attribute 눈_분노:
            "images/characters/hyoju/eyes/angry.png"
        attribute 눈_외면:
            "images/characters/hyoju/eyes/away.png"
        attribute 눈_감음:
            "images/characters/hyoju/eyes/closed.png"
        attribute 눈_실눈:
            "images/characters/hyoju/eyes/laugh_halfopen.png"
        attribute 눈_웃음:
            "images/characters/hyoju/eyes/smile_closed.png"
        attribute 눈_놀람:
            "images/characters/hyoju/eyes/surprised.png"
        attribute 눈_윙크:
            "images/characters/hyoju/eyes/wink.png"

    group mouth:
        pos (1184, 463)
        attribute 입_보통 default:
            "images/characters/hyoju/mouth/normal.png"
        attribute 입_황당:
            "images/characters/hyoju/mouth/absurd.png"
        attribute 입_메롱:
            "images/characters/hyoju/mouth/boo.png"
        attribute 입_찡그림:
            "images/characters/hyoju/mouth/frown.png"
        attribute 입_키스:
            "images/characters/hyoju/mouth/kiss.png"
        attribute 입_폭소:
            "images/characters/hyoju/mouth/laugh.png"
        attribute 입_크게벌림:
            "images/characters/hyoju/mouth/open_large.png"
        attribute 입_벌림:
            "images/characters/hyoju/mouth/open_small.png"
        attribute 입_우쭐:
            "images/characters/hyoju/mouth/proud.png"
        attribute 입_미소:
            "images/characters/hyoju/mouth/smile.png"
        attribute 입_미소치아:
            "images/characters/hyoju/mouth/smile_teeth.png"
        attribute 입_삐침:
            "images/characters/hyoju/mouth/sulk.png"
        attribute 입_혀내밂:
            "images/characters/hyoju/mouth/tongue.png"

    # 앞머리
    always:
        pos (724, 0)
        "images/characters/hyoju/body/bangs.png"

image side 효주 = LayeredImageProxy("효주", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

