#pragma once

#include <SDL_image.h>
#include "base.h"

class Image: public Displayable
{
    public:
        Image(SDL_Renderer* renderer):
            Displayable(renderer)
            {}
        Image(Window* window): Image(window->getRenderer()) {}
        virtual ~Image() {}

        int loadImage(const std::string& path);
        // virtual void display();

    private:
        std::string     mPath;
};
