"""renpy
init -1 python:
"""

def say_arguments_callback(char, *args, **kwargs):
    # renpy.sound.play("flashing.mp3")
    return args, kwargs

def getAvailableDates():
    global gDates
    p = getIdlePopulation() // 1000

    return min(max(0, p - gDates), 120)

def isDateAvailable():
    return getAvailableDates() > 0

# 받침유무판별기
# URL : [렌파이] 한국어 조사 자동으로 바꾸기 ===> https://cafe.naver.com/vmo/102
# 수정: 파이썬 3.0부터는 유니코드가 기본
def finalChecker(korstr):
    # 마지막 한 글자의 유니코드 가져와 '가'와의 거리 구하기
    dec = 0
    for c in reversed(korstr):
        if c >= '가' and c <= '힣':
            dec = ord(c) - ord('가')
            break

    # 첫번째는 종성이 없고 이후로 종성 27개가 배열됨
    # 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'
    # 즉 '가'와의 거리가 28의 배수이면 종성이 없음
    if dec % 28 == 0:
        return False
    else:
        return True

def finalCheckerLo(korstr):
    # 마지막 한 글자의 유니코드 가져와 '가/갈'와의 거리 구하기
    dec = 0
    for c in reversed(korstr):
        if c >= '가' and c <= '힣':
            dec = ord(c) - ord('가')
            break

    # 종성 없음, 혹은 'ㄹ'종성 뒤는 '로', 나머지는 '으로'
    # 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'
    # 즉 '가', 혹은 '갈'과의 거리가 28의 배수이면 '로', 아니면 '으로'
    if dec % 28 == 0:
        return False
    elif dec % 28 == 8:
        return False
    else:
        return True

def ppCommon(tag, argument, contents):
    (kind, str) = contents[-1]

    ret = []

    if finalChecker(str):
        ret = [(renpy.TEXT_TEXT, tag[0])]
    else:
        ret = [(renpy.TEXT_TEXT, tag[1])]

    if argument:
        ret = [(renpy.TEXT_TAG, "color=" + argument)] + contents + [(renpy.TEXT_TAG, "/color")] + ret
    else:
        ret = contents + ret

    return ret        

def ppLo(tag, argument, contents):
    (kind, str) = contents[-1]

    ret = []
    if finalCheckerLo(str):
        ret = [(renpy.TEXT_TEXT, "으로")]
    else:
        ret = [(renpy.TEXT_TEXT, "로")]

    if argument:
        ret = [(renpy.TEXT_TAG, "color=" + argument)] + contents + [(renpy.TEXT_TAG, "/color")] + ret
    else:
        ret = contents + ret
        
    return ret

def ppYa(tag, argument, contents):
    (kind, str) = contents[-1]

    ret = []
    if finalCheckerLo(str):
        ret = [(renpy.TEXT_TEXT, "이야")]
    else:
        ret = [(renpy.TEXT_TEXT, "야")]

    if argument:
        ret = [(renpy.TEXT_TAG, "color=" + argument)] + contents + [(renpy.TEXT_TAG, "/color")] + ret
    else:
        ret = contents + ret
        
    return ret

def ppLa(tag, argument, contents):
    (kind, str) = contents[-1]

    ret = []
    if finalCheckerLo(str):
        ret = [(renpy.TEXT_TEXT, "이라")]
    else:
        ret = [(renpy.TEXT_TEXT, "라")]

    if argument:
        ret = [(renpy.TEXT_TAG, "color=" + argument)] + contents + [(renpy.TEXT_TAG, "/color")] + ret
    else:
        ret = contents + ret
        
    return ret

