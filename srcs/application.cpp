#include "base.h"

int Application::initialize(const int imgFlags)
{
    int ret = 0;

	TRY( SDL_Init( SDL_INIT_VIDEO ) >= 0, EINIT );
    TRY( (IMG_Init(imgFlags) & imgFlags) == imgFlags, EIMGINIT );
    TRY( Font::initializeStatic() == 0, ETTFINIT );

    CATCH(EINIT)
    {
        TRACE("Cannot initialize SDL: %s\n", SDL_GetError());
        ret = -1;
    }
    CATCH(EIMGINIT)
    {
        TRACE("Cannot initialize SDL2 image: %s\n", SDL_GetError());
        ret = -1;
    }
    CATCH(ETTFINIT)
    {
        TRACE("Cannot initialize SDL2 true type fonts: %s\n", SDL_GetError());
        ret = -1;
    }

    FINALLY;
    return ret;
}

void Application::finalize()
{
    TTF_Quit();
    IMG_Quit();
    SDL_Quit();
}

