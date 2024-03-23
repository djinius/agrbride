#pragma once

#include "base.h"

/******************************************************************************
 * 
 * Textbutton: 텍스트버튼 클래스
 * - 속성:
 *  - text    : 버튼에 표기할 구문
 *  - idleColor             : IDLE(마우스 오버 상태가 아닐 때) 배경색상
 *  - hoverColor            : HOVER(마우스 오버 상태) 배경색상
 *  - clickedColor          : 마우스 클릭 때 배경색상
 *  - selectedColor         : 선택됐을 때 배경색상
 *  - selectedHoverColor    : 선택되었고, 마우스 오버 상태일 때 배경색상
 *  - selectedClickedColor  : 선택되었고, 마우스 클릭 상태일 때 배경색상
 *  - insensitiveColor      : 버튼 비활성화 때 배경색상
 * 
 * 기초 생성자: 서피스, 표시 위치, 표기할 텍스트
 * 
 *****************************************************************************/

class TextButton: public Button, public Displayable
{
    public:
        TextButton(SDL_Surface*, SDL_Rect, const std::cstring&);
        virtual ~TextButton() {}

    private:
        virtual void display();

    private:
        SDL_Color BGColor { 255, 50, 50, 255 };
        SDL_Color HoverColor { 50, 50, 255, 255 };
        SDL_Color ClickedColor { 255, 255, 50, 255 };
        SDL_Color AltClickedColor { 255, 255, 255, 255 };
};
