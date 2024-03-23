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

	// width = DM.w;
	// height = DM.h;

    TRY( (mSDLWindow = SDL_CreateWindow(windowName.c_str(), 0, 0, 1920, 1080, SDL_WINDOW_SHOWN)) != NULL );
    TRY( (mSDLRenderer = SDL_CreateRenderer(mSDLWindow, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)) != NULL );
    TRY( (mSDLWindowSurface = SDL_GetWindowSurface(mSDLWindow)) != NULL );

    SDL_FillRect(mSDLWindowSurface, nullptr, SDL_MapRGB(mSDLWindowSurface->format, 40, 40, 40));
    /*
    SDL_SetRenderDrawColor(mSDLRenderer, 40, 40, 40, 0);
    SDL_RenderFillRect(mSDLRenderer, NULL);
    SDL_RenderFlush(mSDLRenderer);
    */

    return 0;

    FINALLY;
    TRACE( "Could not initialize window! SDL Error: %s\n", SDL_GetError() );

    return -1;
}

void Window::beginRender()
{
    SDL_FillRect(mSDLWindowSurface, nullptr, SDL_MapRGB(mSDLWindowSurface->format, 40, 40, 40));
}

void Window::finishRender()
{
    TRACE("Rendering frame again: %p\n", this);
    SDL_UpdateWindowSurface(mSDLWindow);
    /*
    SDL_RenderClear(mSDLRenderer);
    SDL_SetRenderDrawColor(mSDLRenderer, 40, 40, 40, 0);
    SDL_RenderFillRect(mSDLRenderer, NULL);
    SDL_RenderFlush(mSDLRenderer);
    */
}

Window::~Window()
{
	// IMG_Quit();
    SDL_DestroyRenderer(mSDLRenderer);
    SDL_DestroyWindow(mSDLWindow);
	SDL_Quit();
}