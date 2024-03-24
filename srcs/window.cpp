#include <assert.h>
#include "common.h"
#include "base.h"

using namespace std;

Window::Window(const string& windowName)
{
    assert( init(windowName) == 0);
}

int Window::init(const string& windowName)
{
    int ret = 0;
    SDL_DisplayMode DM;

    TRY( SDL_GetCurrentDisplayMode(0, &DM) >= 0, EINIT );

    TRY( (mSDLWindow = SDL_CreateWindow(windowName.c_str(), 0, 0, 1920, 1080, SDL_WINDOW_FULLSCREEN)) != NULL, EINIT );
    TRY( (mSDLRenderer = SDL_CreateRenderer(mSDLWindow, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)) != NULL, EINIT );

    TRY( Font::initializeStatic() == 0, EINIT );

    CATCH(EINIT)
    {
        TRACE("Cannot create window: %s\n", SDL_GetError());
    }

    FINALLY;

    return ret;
}

void Window::beginRender()
{
    SDL_RenderClear(mSDLRenderer);
}

void Window::finishRender()
{
    TRACE("Rendering frame again: %p\n", this);
    SDL_RenderPresent(mSDLRenderer);
}

Window::~Window()
{
    SDL_DestroyRenderer(mSDLRenderer);
    SDL_DestroyWindow(mSDLWindow);
	SDL_Quit();
}