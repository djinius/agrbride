define 말리 = Character('말리', color="#98FF98", image="말리", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayMali")
default maliHSceneEnabled = False

screen sayMali(who, what):
    use sayCommon(who, what, hcolor="#188018")

######
# 정면 - 3285x4063
# 얼굴 - 1470, 442
# 홍조 - 1460, 539
# 그림자 - 1487, 367
# 땀 - 1722, 634
# 놀람마크 - 1313, 129

layeredimage 말리 정면:
    group body:
        attribute 몬무스 default:
            ConditionSwitch(
                "persistent.isStreaming==True", "images/characters/mali/front/monmusu_censored.png",
                "True", "images/characters/mali/front/monmusu.png"
            )

        attribute 일상복1:
            "images/characters/mali/front/comfort.png"
        attribute 일상복2:
            "images/characters/mali/front/sexy.png"
        attribute 한복:
            "images/characters/mali/front/hanbok.png"
        attribute 일상복:
            ConditionSwitch("maliHSceneEnabled", "images/characters/mali/front/comfort.png",
                            "True", "images/characters/mali/mali/sexy.png")

    group face:
        pos (1470, 442)
        attribute 보통 default:
            "images/characters/mali/front/faces/normal.png"
        attribute 입벌림:
            "images/characters/mali/front/faces/normal_open.png"

        attribute 미소1:
            "images/characters/mali/front/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/mali/front/faces/smile_open.png"

        attribute 윙크:
            "images/characters/mali/front/faces/wink_closed.png"

        attribute 장난기1:
            "images/characters/mali/front/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/mali/front/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/mali/front/faces/playful_wink.png"

        attribute 정색:
            "images/characters/mali/front/faces/stern.png"
        attribute 분노1:
            "images/characters/mali/front/faces/angry_open.png"
        attribute 분노2:
            "images/characters/mali/front/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/mali/front/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/mali/front/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/mali/front/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/mali/front/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/mali/front/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/mali/front/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/mali/front/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/mali/front/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/mali/front/faces/painful.png"

    group faceshadow:
        pos (1487, 367)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/mali/front/extras/shadow.png"

    group surprisedmark:
        pos (1313, 129)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/mali/front/extras/surprisedmark.png"

    group sweat:
        pos (1722, 634)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/mali/front/extras/sweat.png"

    group blush:
        pos (1460, 539)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/mali/front/extras/blush.png"

image side 말리 정면 = LayeredImageProxy("말리 정면", Transform(crop=(1100, 0, 1800, 1950), zoom=.4))

######
# 좌측면 - 3285x4063
# 얼굴 - 302, 443
# 홍조 - 291, 524
# 그림자 - 316, 374
# 땀 - 535, 612
# 놀람마크 - 155, 119

layeredimage 말리 좌측면:
    group body:
        attribute 한복 default:
            "images/characters/mali/left/hanbok.png"
        attribute 일상복1:
            "images/characters/mali/left/comfort.png"
        attribute 일상복2:
            "images/characters/mali/left/sexy.png"
        attribute 일상복:
            ConditionSwitch("maliHSceneEnabled", "images/characters/mali/left/comfort.png",
                            "True", "images/characters/mali/left/sexy.png")

    group face:
        pos (302, 443)
        attribute 보통 default:
            "images/characters/mali/left/faces/normal.png"
        attribute 입벌림:
            "images/characters/mali/left/faces/normal_open.png"

        attribute 미소1:
            "images/characters/mali/left/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/mali/left/faces/smile_open.png"

        attribute 윙크:
            "images/characters/mali/left/faces/wink_closed.png"

        attribute 장난기1:
            "images/characters/mali/left/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/mali/left/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/mali/left/faces/playful_wink.png"

        attribute 정색:
            "images/characters/mali/left/faces/stern.png"
        attribute 분노1:
            "images/characters/mali/left/faces/angry_open.png"
        attribute 분노2:
            "images/characters/mali/left/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/mali/left/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/mali/left/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/mali/left/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/mali/left/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/mali/left/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/mali/left/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/mali/left/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/mali/left/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/mali/left/faces/painful.png"

    group faceshadow:
        pos (316, 374)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/mali/left/extras/shadow.png"

    group surprisedmark:
        pos (155, 119)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/mali/left/extras/surprisedmark.png"

    group sweat:
        pos (535, 612)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/mali/left/extras/sweat.png"

    group blush:
        pos (291, 524)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/mali/left/extras/blush.png"

image side 말리 좌측면 = LayeredImageProxy("말리 좌측면", Transform(crop=(0, 0, 1397, 1950), zoom=.4))

######
# 우측면 - 1397x3961
# 얼굴 - 788, 443
# 홍조 - 764, 524
# 그림자 - 794, 374
# 땀 - 847, 612
# 놀람마크 - 1077, 119

layeredimage 말리 우측면:
    group body:
        attribute 한복 default:
            "images/characters/mali/right/hanbok.png"
        attribute 일상복1:
            "images/characters/mali/right/comfort.png"
        attribute 일상복2:
            "images/characters/mali/right/sexy.png"
        attribute 일상복:
            ConditionSwitch("maliHSceneEnabled", "images/characters/mali/right/comfort.png",
                            "True", "images/characters/mali/right/sexy.png")

    group face:
        pos (788, 443)
        attribute 보통 default:
            "images/characters/mali/right/faces/normal.png"
        attribute 입벌림:
            "images/characters/mali/right/faces/normal_open.png"

        attribute 미소1:
            "images/characters/mali/right/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/mali/right/faces/smile_open.png"

        attribute 윙크:
            "images/characters/mali/right/faces/wink_closed.png"

        attribute 장난기1:
            "images/characters/mali/right/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/mali/right/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/mali/right/faces/playful_wink.png"

        attribute 정색:
            "images/characters/mali/right/faces/stern.png"
        attribute 분노1:
            "images/characters/mali/right/faces/angry_open.png"
        attribute 분노2:
            "images/characters/mali/right/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/mali/right/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/mali/right/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/mali/right/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/mali/right/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/mali/right/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/mali/right/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/mali/right/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/mali/right/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/mali/right/faces/painful.png"

    group faceshadow:
        pos (794, 374)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/mali/right/extras/shadow.png"

    group surprisedmark:
        pos (1077, 119)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/mali/right/extras/surprisedmark.png"

    group sweat:
        pos (847, 612)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/mali/right/extras/sweat.png"

    group blush:
        pos (764, 524)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/mali/right/extras/blush.png"

image side 말리 우측면 = LayeredImageProxy("말리 우측면", Transform(crop=(400, 0, 897, 1950), zoom=.4))

