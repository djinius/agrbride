default rosalindName = "???"

define 로잘린드 = Character('rosalindName', dynamic=True, color="#CDC8C3", hcolor="#4D4843", image="로잘린드")

# 정면
# 얼굴 표정요소 좌표: (976, 359)

layeredimage 로잘린드 정면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/rosalind/front/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/rosalind/front/monmusu.png"
        attribute 일상복1:
            "images/characters/rosalind/front/comfort.png"
        attribute 일상복1_무더듬이:
            "images/characters/rosalind/front/comfort_noantannae.png"
        attribute 일상복2:
            "images/characters/rosalind/front/sexy.png"
        attribute 한복:
            "images/characters/rosalind/front/hanbok.png"
        attribute 장옷:
            "images/characters/rosalind/front/hanbok_coat.png"

    group face:
        pos (976, 359)
        attribute 보통 default:
            "images/characters/rosalind/front/faces/normal.png"
        attribute 입벌림:
            "images/characters/rosalind/front/faces/normal_open.png"

        attribute 미소1:
            "images/characters/rosalind/front/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/rosalind/front/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/rosalind/front/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/rosalind/front/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/rosalind/front/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/rosalind/front/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/rosalind/front/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/rosalind/front/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/rosalind/front/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/rosalind/front/faces/playful_wink.png"

        attribute 정색:
            "images/characters/rosalind/front/faces/stern.png"
        attribute 분노1:
            "images/characters/rosalind/front/faces/angry_open.png"
        attribute 분노2:
            "images/characters/rosalind/front/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/rosalind/front/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/rosalind/front/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/rosalind/front/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/rosalind/front/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/rosalind/front/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/rosalind/front/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/rosalind/front/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/rosalind/front/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/rosalind/front/faces/painful.png"

        attribute 하트:
            "images/characters/rosalind/front/faces/hearts.png"

    group faceshadow:
        pos (991, 265)
        attribute 얼굴그림자없음 default:
            Null()
        attribute 얼굴그림자:
            "images/characters/rosalind/front/extras/shadow.png"

    group surprisedmark:
        pos (826, 72)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/rosalind/front/extras/surprisedmark.png"

    group sweat:
        pos (1219, 561)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/rosalind/front/extras/sweat.png"

    group blush:
        pos (971, 478)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/rosalind/front/extras/blush.png"

image side 로잘린드 정면 = LayeredImageProxy("로잘린드 정면", Transform(crop=(700, 0, 1800, 1800), zoom=.4))

# 좌측면
# 얼굴 표정요소 좌표: (650, 366)

layeredimage 로잘린드 좌측면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/rosalind/left/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/rosalind/left/monmusu.png"
        attribute 일상복1:
            "images/characters/rosalind/left/comfort.png"
        attribute 일상복1_무더듬이:
            "images/characters/rosalind/left/comfort_noantannae.png"
        attribute 일상복2:
            "images/characters/rosalind/left/sexy.png"
        attribute 한복:
            "images/characters/rosalind/left/hanbok.png"
        attribute 장옷:
            "images/characters/rosalind/left/hanbok_coat.png"

    group face:
        pos (650, 366)
        attribute 보통 default:
            "images/characters/rosalind/left/faces/normal.png"
        attribute 입벌림:
            "images/characters/rosalind/left/faces/normal_open.png"

        attribute 미소1:
            "images/characters/rosalind/left/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/rosalind/left/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/rosalind/left/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/rosalind/left/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/rosalind/left/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/rosalind/left/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/rosalind/left/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/rosalind/left/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/rosalind/left/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/rosalind/left/faces/playful_wink.png"

        attribute 정색:
            "images/characters/rosalind/left/faces/stern.png"
        attribute 분노1:
            "images/characters/rosalind/left/faces/angry_open.png"
        attribute 분노2:
            "images/characters/rosalind/left/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/rosalind/left/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/rosalind/left/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/rosalind/left/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/rosalind/left/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/rosalind/left/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/rosalind/left/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/rosalind/left/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/rosalind/left/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/rosalind/left/faces/painful.png"

        attribute 하트:
            "images/characters/rosalind/left/faces/hearts.png"

    group faceshadow:
        pos (590, 135)
        attribute 그림자없음 default:
            Null()
        attribute 그림자:
            "images/characters/rosalind/left/extras/shadow.png"

    group surprisedmark:
        pos (494, 83)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/rosalind/left/extras/surprisedmark.png"

    group sweat:
        pos (887, 572)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/rosalind/left/extras/sweat.png"

    group blush:
        pos (644, 487)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/rosalind/left/extras/blush.png"


image side 로잘린드 좌측면 = LayeredImageProxy("로잘린드 좌측면", Transform(crop=(600, 0, 1900, 2100), zoom=.4))

# 우측면
# 얼굴 표정요소 좌표: (950, 366)


layeredimage 로잘린드 우측면:
    group wing:
        attribute 날개없음 default:
            Null()
        attribute 날개:
            "images/characters/rosalind/right/wing.png"

    group body:
        attribute 몬무스 default:
            "images/characters/rosalind/right/monmusu.png"
        attribute 일상복1:
            "images/characters/rosalind/right/comfort.png"
        attribute 일상복1_무더듬이:
            "images/characters/rosalind/right/comfort_noantannae.png"
        attribute 일상복2:
            "images/characters/rosalind/right/sexy.png"
        attribute 한복:
            "images/characters/rosalind/right/hanbok.png"
        attribute 장옷:
            "images/characters/rosalind/right/hanbok_coat.png"

    group face:
        pos (950, 366)
        attribute 보통 default:
            "images/characters/rosalind/right/faces/normal.png"
        attribute 입벌림:
            "images/characters/rosalind/right/faces/normal_open.png"

        attribute 미소1:
            "images/characters/rosalind/right/faces/smile_closed.png"
        attribute 미소2:
            "images/characters/rosalind/right/faces/smile_open.png"

        attribute 웃음1:
            "images/characters/rosalind/right/faces/laugh_allclosed.png"
        attribute 웃음2:
            "images/characters/rosalind/right/faces/laugh_closedeyes.png"
        attribute 웃음3:
            "images/characters/rosalind/right/faces/laugh_teeth.png"

        attribute 윙크1:
            "images/characters/rosalind/right/faces/wink_closed.png"
        attribute 윙크2:
            "images/characters/rosalind/right/faces/wink_open.png"

        attribute 장난기1:
            "images/characters/rosalind/right/faces/playful_closed.png"
        attribute 장난기2:
            "images/characters/rosalind/right/faces/playful_open.png"
        attribute 장난기3:
            "images/characters/rosalind/right/faces/playful_wink.png"

        attribute 정색:
            "images/characters/rosalind/right/faces/stern.png"
        attribute 분노1:
            "images/characters/rosalind/right/faces/angry_open.png"
        attribute 분노2:
            "images/characters/rosalind/right/faces/angry_teeth.png"

        attribute 놀람1:
            "images/characters/rosalind/right/faces/surprised_small.png"
        attribute 놀람2:
            "images/characters/rosalind/right/faces/surprised_large.png"

        attribute 풀죽음1:
            "images/characters/rosalind/right/faces/timid_closed.png"
        attribute 풀죽음2:
            "images/characters/rosalind/right/faces/timid_open.png"
        attribute 풀죽음3:
            "images/characters/rosalind/right/faces/timid_tongue.png"

        attribute 황당1:
            "images/characters/rosalind/right/faces/absurd_closed.png"
        attribute 황당2:
            "images/characters/rosalind/right/faces/absurd_open.png"
        attribute 황당3:
            "images/characters/rosalind/right/faces/absurd_tongue.png"

        attribute 고통:
            "images/characters/rosalind/right/faces/painful.png"

        attribute 하트:
            "images/characters/rosalind/right/faces/hearts.png"

    group faceshadow:
        pos (837, 135)
        attribute 그림자없음 default:
            Null()
        attribute 그림자:
            "images/characters/rosalind/right/extras/shadow.png"

    group surprisedmark:
        pos (1274, 83)
        attribute 놀람마크없음 default:
            Null()
        attribute 놀람마크:
            "images/characters/rosalind/right/extras/surprisedmark.png"

    group sweat:
        pos (1029, 572)
        attribute 땀없음 default:
            Null()
        attribute 땀:
            "images/characters/rosalind/right/extras/sweat.png"

    group blush:
        pos (945, 487)
        attribute 홍조없음 default:
            Null()
        attribute 홍조:
            "images/characters/rosalind/right/extras/blush.png"


image side 로잘린드 우측면 = LayeredImageProxy("로잘린드 우측면", Transform(crop=(600, 0, 1900, 2100), zoom=.4))
