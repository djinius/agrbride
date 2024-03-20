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
    int resultCode;
    SDL_DisplayMode DM;
    int width, height;

    resultCode = SDL_Init( SDL_INIT_VIDEO );
	TRY( resultCode >= 0 );

	resultCode = SDL_GetCurrentDisplayMode(0, &DM);
    TRY( resultCode >= 0 );

	width = DM.w;
	height = DM.h;

    mSDLWindow = SDL_CreateWindow(windowName.c_str(), 0, 0, width, height, SDL_WINDOW_SHOWN);
    TRY(mSDLWindow != NULL);

    mSDLWindowSurface = SDL_GetWindowSurface(mSDLWindow);
    TRY(mSDLWindowSurface != NULL);

    SDL_FillRect(mSDLWindowSurface, nullptr, SDL_MapRGB(mSDLWindowSurface->format, 40, 40, 40));

    return 0;

    FINALLY;
    TRACE( "Could not initialize window! SDL Error: %s\n", SDL_GetError() );

    return -1;
}

void Window::renderFrame()
{
    SDL_UpdateWindowSurface(mSDLWindow);
}