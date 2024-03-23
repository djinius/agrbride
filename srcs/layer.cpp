#include "base.h"
#include "common.h"

bool Layer::handleEvent(const SDL_Event* event)
{
    bool ret = false;

    for (const auto handler : mSubscribers)
    {
        TRACE( "Event event with %p\n", handler );
        if( handler->handleEvent(event) )
        {
            ret = true;
            break;
        }
    }

    for (const auto displayable : mDisplayables)
    {
        TRACE( "Display %p\n", displayable );
        displayable->display();
    }

    return ret;
}
