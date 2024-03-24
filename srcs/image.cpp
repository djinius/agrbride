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
    setSize(iSurface->w, iSurface->h);
    setColorKey(iSurface, SDL_TRUE, SDL_MapRGBA(iSurface->format, 0, 0, 0, 0));
    TRY( createTexture(iSurface) != nullptr );

    freeSurface(iSurface);

    return 0;

    FINALLY;
    freeSurface(iSurface);
    destroyTexture();
    return -1;
}
