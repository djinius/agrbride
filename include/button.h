#pragma once

#include "base.h"

class Button: public EventReceiver, public Displayable
{
    public:
        Button(SDL_Renderer*, SDL_Rect);
        virtual ~Button() {}
        virtual bool handleEvent(const SDL_Event*);
        virtual void display() = 0;

    private:
        virtual bool isMouseInBound(const int, const int);

    private:
        SDL_Rect mRect;
};
