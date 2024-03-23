#pragma once

#include "base.h"

class Text: public Displayable
{
    public:
        Text(Window* window, const std::string& str, SDL_Color fgColor): Text(window, str, Font::getDefaultFont(), fgColor) {}
        Text(Window*, const std::string&, Font* = Font::getDefaultFont(), SDL_Color = {255, 255, 255}, SDL_Color = {0, 0, 0, 0});
        virtual ~Text()
        {
            SDL_FreeSurface(mTextSurface);
        }
        virtual void display();
        void update(const std::string&);

    private:
        SDL_Surface*    mTextSurface;
        std::string     mString;
        Font*           mFont;
        SDL_Color       mFGColor;
        SDL_Color       mBGColor;
};
