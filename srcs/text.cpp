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

void Text::update(const std::string& str)
{
    auto [r, g, b, a] = mBGColor;
    SDL_Surface* textSurface = nullptr;
    mString = str;

    TRY( mString.length() > 0, EZEROLENGTH );
    TRY( (textSurface  = TTF_RenderUTF8_LCD(*mFont, str.c_str(), mFGColor, mBGColor)) != nullptr, ERENDERFAILED );
    if( a == 0 )
    {
        setColorKey(textSurface, SDL_TRUE, SDL_MapRGBA(textSurface->format, r, g, b, a));
    }

    TRY( createTexture(textSurface) != nullptr, ETEXTURE );
    setSize(textSurface);

    CATCH(EZEROLENGTH)
    {
        TRACE("Cannot render zero-length string.\n");
        destroyTexture();
        setSize(0, 0);
    }

    CATCH(ERENDERFAILED)
    {
        TRACE("Cannot render UTF8 text(%s): %s\n", mString.c_str(), SDL_GetError());
        setSize(0, 0);
    }

    CATCH(ETEXTURE)
    {
        TRACE("Cannot create texture: %s\n", SDL_GetError());
        setSize(0, 0);
    }

    FINALLY;

    if( textSurface != nullptr )
    {
        freeSurface(textSurface);
    }
}