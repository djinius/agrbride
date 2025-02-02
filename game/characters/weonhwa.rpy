default wonhwaName = "???"

define 원화 = Character('wonhwaName', dynamic=True, color="#FF007F", image="원화", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayWonhwa")

screen sayWonhwa(who, what):
    use sayCommon(who, what, hcolor="#8F003F")

image 원화 몬무스 = "images/ai/characters/standings/weonhwa.png"
