#if !defined(__WINDOW_H__)
#define __WINDOW_H__

#include <string>
#include <SDL.h>

using namespace std;

class Window
{
    public:
        Window() {}

        void init(string windowName);
        void renderFrame();

    private:
        SDL_Window* mSDLWindow { nullptr };
        SDL_Surface* mSDLWindowSurface { nullptr };
};

#endif