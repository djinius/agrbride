#if !defined(__LAYER_H__)
#define __LAYER_H__

#include <SDL.h>

class Layer
{
    public:
        virtual bool handleEvent(const SDL_Event* event) = 0;
};

#endif