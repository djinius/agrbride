default myName = '나'

define 독백 = Character(None, color="#FFFFFF", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayThink")
define 주인공 = Character('myName', dynamic=True, color="#FFFFFF", ctc="ctc35Blink", ctc_position="nestled-close", screen="sayMyself")

screen sayThink(who, what):
    use sayCommon(who, what, hcolor="#444", bg="gui/think.png")

screen sayMyself(who, what):
    use sayCommon(who, what, hcolor="#000")