define 효주 = Character('효주', color="#FFE600", image="효주", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayHyoju")
default hyojuHSceneEnabled = False

screen sayHyoju(who, what):
    use sayCommon(who, what, hcolor="#8F7600")

layeredimage 효주 정면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/hyoju/front/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/hyoju/front/monmusu.png"
        attribute 일상복1:
            "images/characters/hyoju/front/comfort.png"
        attribute 일상복1_무자켓:
            "images/characters/hyoju/front/comfort_nojacket.png"
        attribute 일상복2:
            "images/characters/hyoju/front/sexy.png"
        attribute 한복:
            "images/characters/hyoju/front/hanbok.png"
        attribute 일상복:
            ConditionSwitch("hyojuHSceneEnabled", "images/characters/hyoju/front/comfort.png",
                            "True", "images/characters/hyoju/front/sexy.png")

    group face:
        pos (971, 378)
        attribute 보통 default:
            "images/characters/hyoju/front/faces/normal.png"
        attribute 입벌림:
            "images/characters/hyoju/front/faces/normal_open.png"

        attribute 미소1:
            "images/characters/hyoju/front/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/hyoju/front/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/hyoju/front/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/hyoju/front/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/hyoju/front/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/hyoju/front/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/hyoju/front/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/hyoju/front/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/hyoju/front/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/hyoju/front/faces/playful_wink.png"

        attribute 정색:
            "images/characters/hyoju/front/faces/stern.png"
        attribute 분노1:
            "images/characters/hyoju/front/faces/angry_open.png"
        attribute 분노2:
            "images/characters/hyoju/front/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/hyoju/front/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/hyoju/front/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/hyoju/front/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/hyoju/front/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/hyoju/front/faces/timid_tongue.png"

    group faceshadow:
        pos (991, 328)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/hyoju/front/extras/shadow.png"

    group surprisedmark:
        pos (776, 139)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/hyoju/front/extras/surprisedmark.png"

    group sweat:
        pos (1230, 565)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/hyoju/front/extras/sweat.png"

    group blush:
        pos (991, 446)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/hyoju/front/extras/blush.png"

image side 효주 정면 = LayeredImageProxy("효주 정면", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

layeredimage 효주 좌측면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/hyoju/left/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/hyoju/left/monmusu.png"
        attribute 일상복1:
            "images/characters/hyoju/left/comfort.png"
        attribute 일상복1_무자켓:
            "images/characters/hyoju/left/comfort_nojacket.png"
        attribute 일상복2:
            "images/characters/hyoju/left/sexy.png"
        attribute 한복:
            "images/characters/hyoju/left/hanbok.png"
        attribute 일상복:
            ConditionSwitch("hyojuHSceneEnabled", "images/characters/hyoju/left/comfort.png",
                            "True", "images/characters/hyoju/left/sexy.png")

    group face:
        pos (578, 378)
        attribute 보통 default:
            "images/characters/hyoju/left/faces/normal.png"
        attribute 입벌림:
            "images/characters/hyoju/left/faces/normal_open.png"

        attribute 미소1:
            "images/characters/hyoju/left/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/hyoju/left/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/hyoju/left/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/hyoju/left/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/hyoju/left/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/hyoju/left/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/hyoju/left/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/hyoju/left/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/hyoju/left/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/hyoju/left/faces/playful_wink.png"

        attribute 정색:
            "images/characters/hyoju/left/faces/stern.png"
        attribute 분노1:
            "images/characters/hyoju/left/faces/angry_open.png"
        attribute 분노2:
            "images/characters/hyoju/left/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/hyoju/left/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/hyoju/left/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/hyoju/left/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/hyoju/left/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/hyoju/left/faces/timid_tongue.png"

    group faceshadow:
        pos (383, 139)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/hyoju/left/extras/shadow.png"

    group surprisedmark:
        pos (383, 139)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/hyoju/left/extras/surprisedmark.png"

    group sweat:
        pos (383, 139)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/hyoju/left/extras/sweat.png"

    group blush:
        pos (383, 139)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/hyoju/left/extras/blush.png"

image side 효주 좌측면 = LayeredImageProxy("효주 좌측면", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

layeredimage 효주 우측면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/hyoju/right/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/hyoju/right/monmusu.png"
        attribute 일상복1:
            "images/characters/hyoju/right/comfort.png"
        attribute 일상복1_무자켓:
            "images/characters/hyoju/right/comfort_nojacket.png"
        attribute 일상복2:
            "images/characters/hyoju/right/sexy.png"
        attribute 한복:
            "images/characters/hyoju/right/hanbok.png"
        attribute 일상복:
            ConditionSwitch("hyojuHSceneEnabled", "images/characters/hyoju/right/comfort.png",
                            "True", "images/characters/hyoju/right/sexy.png")

    group face:
        pos (1081, 378)
        attribute 보통 default:
            "images/characters/hyoju/right/faces/normal.png"
        attribute 입벌림:
            "images/characters/hyoju/right/faces/normal_open.png"

        attribute 미소1:
            "images/characters/hyoju/right/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/hyoju/right/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/hyoju/right/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/hyoju/right/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/hyoju/right/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/hyoju/right/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/hyoju/right/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/hyoju/right/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/hyoju/right/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/hyoju/right/faces/playful_wink.png"

        attribute 정색:
            "images/characters/hyoju/right/faces/stern.png"
        attribute 분노1:
            "images/characters/hyoju/right/faces/angry_open.png"
        attribute 분노2:
            "images/characters/hyoju/right/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/hyoju/right/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/hyoju/right/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/hyoju/right/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/hyoju/right/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/hyoju/right/faces/timid_tongue.png"

    group faceshadow:
        pos (1080, 139)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/hyoju/right/extras/shadow.png"

    group surprisedmark:
        pos (1080, 139)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/hyoju/right/extras/surprisedmark.png"

    group sweat:
        pos (1080, 139)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/hyoju/right/extras/sweat.png"

    group blush:
        pos (1080, 139)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/hyoju/right/extras/blush.png"

image side 효주 우측면 = LayeredImageProxy("효주 우측면", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

