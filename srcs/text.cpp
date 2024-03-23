#include "text.h"
#include "common.h"

Text::Text(Window*          window,
        const std::string&  str,
        Font*               font,
        SDL_Color           fgColor,
        SDL_Color           bgColor):
    Displayable(window), mFont(font), mFGColor(fgColor), mBGColor(bgColor)
{
    update(str);
}

void Text::display()
{
    SDL_Rect dstRect;
    TRY( mTextSurface != nullptr );
    dstRect = calcXYPos(mTextSurface);

    TRACE("Text(%s) surface size: %d, %d\n", mString.c_str(), dstRect.x, dstRect.y);
    blitSurface(mTextSurface, NULL, &dstRect);

    FINALLY;
}

void Text::update(const std::string& str)
{
    mString = str;

    auto [r, g, b, a] = mBGColor;
    TRY_RAISE( (mTextSurface  = TTF_RenderUTF8_LCD(*mFont, str.c_str(), mFGColor, mBGColor)) != nullptr, ERENDERFAILED );
    if( a == 0 )
    {
        SDL_SetColorKey(mTextSurface, SDL_TRUE, SDL_MapRGBA(mTextSurface->format, r, g, b, a));
    }
    display();

    CATCH(ERENDERFAILED)
    {
        TRACE("Cannot render UTF8 text(%s): %s\n", mString.c_str(), SDL_GetError());
    }

    FINALLY;
}