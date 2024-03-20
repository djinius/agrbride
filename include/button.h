#pragma once

#include "base.h"

class Button: public EventReceiver, public Displayable
{
    public:
        Button(SDL_Surface*);
        virtual ~Button() {}
        virtual bool handleEvent(const SDL_Event*);

    private:
        virtual bool isMouseInBound(const int, const int);
        virtual void display();

    private:
        bool isHovered;
        bool isClicked;
        bool isAltClicked;
        SDL_Color BGColor { 255, 50, 50, 255 };
        SDL_Color HoverColor { 50, 50, 255, 255 };
        SDL_Color ClickedColor { 255, 255, 50, 255 };
        SDL_Color AltClickedColor { 255, 255, 255, 255 };
        SDL_Rect Rect { 50, 50, 50, 50 };        
};
