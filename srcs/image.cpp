#include "image.h"
#include "common.h"

using namespace std;

int Image::loadImage(const string& path)
{
    SDL_Surface* iSurface = nullptr;
    int ret = 0;

    TRY( (iSurface = IMG_Load(path.c_str())) != nullptr, ELOAD );
    setSize(iSurface->w, iSurface->h);
    setColorKey(iSurface, SDL_TRUE, SDL_MapRGBA(iSurface->format, 0, 0, 0, 0));
    TRY( createTexture(iSurface) != nullptr, ETEXTURE );

    CATCH(ELOAD)
    {
        TRACE("Loading %s failed: %s\n", path.c_str(), getError());
        destroyTexture();
        ret = -1;
    }

    CATCH(ETEXTURE)
    {
        TRACE("Loading %s failed: %s\n", path.c_str(), getError());
        destroyTexture();
        ret = -1;
    }

    FINALLY;
    freeSurface(iSurface);
    
    return ret;
}
