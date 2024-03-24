#include "common.h"
#include "button.h"

Button::Button(SDL_Renderer* renderer, SDL_Rect rect):
    Displayable(renderer), mRect(rect)
{
}

bool Button::isMouseInBound(const int x, const int y)
{
    TRACE("Bound checker: (%d, %d - %d, %d) {%d, %d}\n",mRect.x,mRect.y,mRect.w,mRect.h, x, y );
    if(x <mRect.x ) return false;
    if(x >mRect.x +mRect.w ) return false;
    if(y <mRect.y ) return false;
    if(y >mRect.y +mRect.h ) return false;

    return true;
}

bool Button::handleEvent(const SDL_Event* event)
{
    bool ret = false;

    if( !getSensitive() ) return false;

    switch( event->type )
    {
        case SDL_MOUSEBUTTONDOWN:
            switch( event->button.button )
            {
                case SDL_BUTTON_LEFT:
                    if( getHovered() )
                    {
                        TRACE("Left button down! updating...\n");
                        setClicked(true);
                        display();
                        ret = this->clickedHandler();
                    }
                    break;
                case SDL_BUTTON_RIGHT:
                    if( getHovered() )
                    {
                        TRACE("Right button down! updating...\n");
                        setAltClicked();
                        display();
                        ret = this->altClickedHandler();
                    }
                    break;
            }
            break;

        case SDL_MOUSEBUTTONUP:
            switch( event->button.button )
            {
                case SDL_BUTTON_LEFT:
                    if( getHovered() )
                    {
                        TRACE("Left button up! updating...\n");
                        setClicked(false);
                        display();
                        ret = this->releasedHandler();
                    }
                    break;
                case SDL_BUTTON_RIGHT:
                    if( getHovered() )
                    {
                        TRACE("Right button up! updating...\n");
                        setAltClicked(false);
                        display();
                        ret = this->altReleasedHandler();
                    }
                    break;
            }
            break;

        case SDL_MOUSEMOTION:
            bool mouseHovered = isMouseInBound(event->motion.x, event->motion.y);
            if( getHovered() && (mouseHovered == false) )
            {
                setHovered(false);
                setClicked(false);
                setAltClicked(false);
                display();
                ret = this->unhoveredHandler();
            }
            else if( !getHovered() && (mouseHovered == true) )
            {
                setHovered();
                display();
                ret = this->hoveredHandler();
            }
            break;
    }

    return ret;
}

