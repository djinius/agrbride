init python:
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id

        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)

    class ClearText(Action):
        def __init__(self,screen_name, input_id):
            self.screen_name=screen_name
            self.input_id=input_id

        def __call__(self):
            cs = renpy.get_screen(self.screen_name)
            inputWindow = renpy.get_widget(self.screen_name, self.input_id)

            if inputWindow:
                inputWindow.caret_pos = 0
                inputWindow.update_text("", True)

    class BSText(Action):
        def __init__(self,screen_name, input_id):
            self.screen_name=screen_name
            self.input_id=input_id

        def __call__(self):
            cs = renpy.get_screen(self.screen_name)
            inputWindow = renpy.get_widget(self.screen_name, self.input_id)

            if inputWindow:
                res = str(inputWindow.content)
                if inputWindow.caret_pos > 0:
                    res = res[0:(inputWindow.caret_pos-1)] + res[inputWindow.caret_pos:]
                    inputWindow.caret_pos -= 1
                    inputWindow.update_text(res, True)

    class SpaceText(Action):
        def __init__(self,screen_name, input_id):
            self.screen_name=screen_name
            self.input_id=input_id

        def __call__(self):
            inputWindow = renpy.get_widget(self.screen_name,self.input_id)
            if inputWindow:
                res = str(inputWindow.content)
                inputWindow.caret_pos += 1
                inputWindow.update_text(res + " ", True)

    koreanF = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    koreanM = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    koreanL = "　ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

    class AddKorean(Action):
        def __init__(self, screen_name, input_id, first, middle, last):
            super(AddKorean, self).__init__()
            self.screen_name = screen_name
            self.input_id = input_id
            self.first = first
            self.middle = middle
            self.last = last

        def __call__(self):
            if not self.get_sensitive():
                return

            cs = renpy.get_screen(self.screen_name)
            inputWindow = renpy.get_widget(self.screen_name, self.input_id)

            if inputWindow:
                res = str(inputWindow.content)

                if self.middle is None and self.last is None:
                    c = koreanF[self.first]
                    res = res[0:inputWindow.caret_pos] + c + res[inputWindow.caret_pos:]
                    inputWindow.caret_pos += 1
                else:
                    c = chr(0xAC00 + self.first * 588 + self.middle * 28 + self.last)
                    res = res[0:(inputWindow.caret_pos - 1)] + c + res[inputWindow.caret_pos:]

                inputWindow.update_text(res, True)

    class AddKoreanFirst(AddKorean):
        def __init__(self, screen_name, input_id, first):
            super(AddKoreanFirst, self).__init__(screen_name, input_id, first, None, None)

    class AddKoreanMiddle(AddKorean):
        def __init__(self, screen_name, input_id, first, middle):
            super(AddKoreanMiddle, self).__init__(screen_name, input_id, first, middle, 0)

        def get_sensitive(self):
            return (self.first is not None) and (self.middle is not None)

    class AddKoreanLast(AddKorean):
        def __init__(self, screen_name, input_id, first, middle, last):
            super(AddKoreanLast, self).__init__(screen_name, input_id, first, middle, last)

        def get_sensitive(self):
            return (self.first is not None) and (self.middle is not None)

    def getKoreanSyllable(first, middle, last = 0):
        if last is None:
            last = 0

        if first is None:
            if middle is not None:
                return koreanM[middle]
            else:
                return koreanL[last]
        elif middle is None:
            return koreanL[last]
        else:
            return chr(0xAC00 + first * 588 + middle * 28 + last)

screen koreaninput(prompt):

    default koreanF = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    default koreanM = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    default koreanL = "　ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

    default first = None
    default middle = None
    default last = None

    style_prefix "koreaninput"

    add Solid("#222C")

    vbox:
        align (.5, .5)
        spacing 10

        text prompt style "input_prompt"
        input id "inputstr":
            font "NEXON Lv2 Gothic Medium.ttf"
            size 50

        hbox:
            xalign .5
            style_prefix "koreaninputsyallbles"
            spacing 30

            grid 5 6:
                for n, i in enumerate(koreanF):
                    textbutton i:
                        action [AddKoreanFirst("koreaninput", "inputstr", n), SetLocalVariable("first", n)]
                        text_size 30

            grid 5 6:
                for n, m in enumerate(koreanM):
                    textbutton getKoreanSyllable(first, n, 0):
                        action [AddKoreanMiddle("koreaninput", "inputstr", first, n), SetLocalVariable("middle", n)]

            grid 5 6:
                for n, l in enumerate(koreanL):
                    textbutton getKoreanSyllable(first, middle, n):
                        action [AddKoreanLast("koreaninput", "inputstr", first, middle, n), SetLocalVariable("last", n)]

        hbox:
            textbutton "깨끗이":
                xalign .5
                action ClearText("koreaninput", "inputstr")

            textbutton "지우기":
                xalign .5
                action BSText("koreaninput", "inputstr")

            textbutton "띄우기":
                xalign .5
                action SpaceText("koreaninput", "inputstr")

        textbutton "완료":
            xalign .5
            action GetText("koreaninput", "inputstr")

style koreaninput_vbox:
    align (.5, .5)

style koreaninput_text:
    xalign .5
    font "NEXON Lv2 Gothic Medium.ttf"

style koreaninput_hbox:
    xalign .5

style koreaninputsyallbles_grid:
    xalign .5
    spacing 5

style koreaninputsyllables_button:
    align (.5, .5)
    xysize (30, 30)

style koreaninputsyllables_button_text:
    size 30
    font "NEXON Lv2 Gothic Medium.ttf"
