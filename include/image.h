#pragma once

#include <SDL_image.h>
#include "base.h"

class Image: public Displayable
{
    public:
        Image(SDL_Surface* surface = nullptr, SDL_Renderer* renderer = nullptr):
            Displayable(surface, renderer), mOptimizedSurface(nullptr)
            {}
        Image(Window* window): Image(window->getSurface(), window->getRenderer()) {}
        ~Image() { if(mOptimizedSurface != nullptr) SDL_FreeSurface(mOptimizedSurface); }

        int loadImage(const std::string& path);
        virtual void display();

    public:
        int initializeStatic(const int = IMG_INIT_JPG | IMG_INIT_PNG);
        void destroyStatic();

    private:
        std::string     mPath;
        SDL_Surface*    mOptimizedSurface;
};
