default sunnaName = "???"

define 수나 = Character('sunnaName', dynamic=True, color="#FF66CC", hcolor="#803366", image="수나", ctc="ctc35Blink", ctc_position="nestled-close", screen="saySunna")

screen saySunna(who, what):
    use sayCommon(who, what, "#803366")

image 수나 몬무스 = "images/ai/characters/standings/sunna.png"

image side 수나 몬무스 = Transform("images/ai/characters/standings/sunna.png", zoom=.5)
