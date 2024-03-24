#include "base.h"
#include "common.h"

void Displayable::moveTo(const int xp, const int yp, const double xa, const double ya)
{
    mXPos = xp;
    mYPos = yp;
    mXAnchor = xa;
    mYAnchor = ya;
}

SDL_Rect Displayable::calcXYPos()
{
    int w = mW, h = mH;
    int x = mXPos, y = mYPos;

    x = mXPos;
    y = mYPos;
    x -= (int)(mXAnchor * w);
    y -= (int)(mYAnchor * h);

    TRACE("SDL_Rect result: (%d, %d)/(%g, %g)*(%d, %d) => (%d, %d)\n", mXPos, mYPos, mXAnchor, mYAnchor, w, h, x, y);
    return SDL_Rect{x, y, w, h};
}

void Displayable::display()
{
    SDL_Rect dstRect = calcXYPos();
    TRY( mTexture != nullptr );
    SDL_RenderCopy(mSDLRenderer, mTexture, NULL, &dstRect);

    FINALLY;
}
