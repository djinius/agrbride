#pragma once

#include "base.h"
#include "common.h"

class KeyHandler: public EventReceiver
{
    public:
        virtual bool handleEvent(const SDL_Event* event)
        {
            bool ret = false;

            switch( event->type )
            {
                case SDL_KEYDOWN:
                    TRACE("Key down: %d\n", event->key.keysym.sym);
                    ret = keyPressed(event->key.keysym.sym, true);
                    break;
                case SDL_KEYUP:
                    TRACE("Key up  : %d\n", event->key.keysym.sym);
                    ret = keyPressed(event->key.keysym.sym, false);
                    break;
                default:
                    break;
            }

            return ret;
        }
};
