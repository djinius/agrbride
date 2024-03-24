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
    SDL_DisplayMode DM;

	TRY( SDL_Init( SDL_INIT_VIDEO ) >= 0 );
    TRY( Font::initializeStatic() == 0 );
    TRY( SDL_GetCurrentDisplayMode(0, &DM) >= 0 );

    TRY( (mSDLWindow = SDL_CreateWindow(windowName.c_str(), 0, 0, DM.w, DM.h, SDL_WINDOW_SHOWN)) != NULL );
    TRY( (mSDLRenderer = SDL_CreateRenderer(mSDLWindow, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)) != NULL );
    TRY( (mSDLWindowSurface = SDL_GetWindowSurface(mSDLWindow)) != NULL );

    return 0;

    FINALLY;
    TRACE( "Could not initialize window! SDL Error: %s\n", SDL_GetError() );

    return -1;
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