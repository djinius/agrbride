#include "base.h"
#include "common.h"

void Displayable::moveTo(const int xp, const int yp, const double xa, const double ya)
{
    mXPos = xp;
    mYPos = yp;
    mXAnchor = xa;
    mYAnchor = ya;
}

SDL_Rect Displayable::calcXYPos(SDL_Surface* sf)
{
    if( sf == nullptr )
    {
        TRACE("No surface: (0, 0, 0, 0)\n");
        return SDL_Rect{0, 0, 0, 0};
    }
    else
    {
        int w = sf->w;
        int h = sf->h;

        int x = mXPos;
        int y = mYPos;

        x -= (int)(mXAnchor * w);
        y -= (int)(mYAnchor * h);

        TRACE("SDL_Rect result: (%d, %d)/(%g, %g)*(%d, %d) => (%d, %d)\n", mXPos, mYPos, mXAnchor, mYAnchor, w, h, x, y);
        return SDL_Rect{x, y, w, h};
    }
}