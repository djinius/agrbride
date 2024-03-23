#include "image.h"
#include "common.h"

using namespace std;

int Image::initializeStatic(const int imgFlags)
{
    TRY( (IMG_Init(imgFlags) & imgFlags) == imgFlags );
    return 0;

    FINALLY;
    TRACE("Cannot initialize SDL2 image: %s\n", SDL_GetError());
    return -1;
}

void Image::destroyStatic()
{
    IMG_Quit();
}

int Image::loadImage(const string& path)
{
    SDL_Surface* iSurface = nullptr;
    TRY( (iSurface = IMG_Load(path.c_str())) != nullptr );
    TRY( (mOptimizedSurface = convertSurface(iSurface)) != nullptr );
    SDL_SetColorKey(mOptimizedSurface, SDL_TRUE, SDL_MapRGBA(mOptimizedSurface->format, 0, 0, 0, 0));

    SDL_FreeSurface(iSurface);

    return 0;

    FINALLY;
    if( iSurface != nullptr ) SDL_FreeSurface(iSurface);
    return -1;
}

void Image::display()
{
    SDL_Rect dstRect;
    TRY( mOptimizedSurface != nullptr );
    dstRect = calcXYPos(mOptimizedSurface);
    blitSurface(mOptimizedSurface, NULL, &dstRect);

    FINALLY;
}
