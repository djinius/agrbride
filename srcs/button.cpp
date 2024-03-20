#include "common.h"
#include "button.h"

Button::Button(SDL_Surface* surface):
    Displayable(surface), isHovered(false), isClicked(false), isAltClicked(false)
{
    display();
}

bool Button::isMouseInBound(const int x, const int y)
{
    TRACE("Bound checker: (%d, %d - %d, %d) {%d, %d}\n", Rect.x, Rect.y, Rect.w, Rect.h, x, y );
    if(x < Rect.x ) return false;
    if(x > Rect.x + Rect.w ) return false;
    if(y < Rect.y ) return false;
    if(y > Rect.y + Rect.h ) return false;

    return true;
}

void Button::display()
{
    auto [r, g, b, a] { isClicked? ClickedColor: isAltClicked? AltClickedColor: isHovered? HoverColor : BGColor };
    TRACE("Button color code: %d %d %d %d\n", r, g, b, a);
    SDL_FillRect(mSDLWindowSurface, &Rect, SDL_MapRGB(mSDLWindowSurface->format, r, g, b));
}

bool Button::handleEvent(const SDL_Event* event)
{
    bool ret = false;

    switch( event->type )
    {
        case SDL_MOUSEBUTTONDOWN:
            switch( event->button.button )
            {
                case SDL_BUTTON_LEFT:
                    if( isHovered )
                    {
                        TRACE("Left button down! updating...\n");
                        isClicked = true;
                        display();
                        ret = this->clickedHandler();
                    }
                    break;
                case SDL_BUTTON_RIGHT:
                    if( isHovered )
                    {
                        TRACE("Right button down! updating...\n");
                        isAltClicked = true;
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
                    if( isHovered )
                    {
                        TRACE("Left button up! updating...\n");
                        isClicked = false;
                        display();
                        ret = this->releasedHandler();
                    }
                    break;
                case SDL_BUTTON_RIGHT:
                    if( isHovered )
                    {
                        TRACE("Right button up! updating...\n");
                        isAltClicked = false;
                        display();
                        ret = this->altReleasedHandler();
                    }
                    break;
            }
            break;

        case SDL_MOUSEMOTION:
            bool mouseHovered = isMouseInBound(event->motion.x, event->motion.y);
            if( (isHovered == true) && (mouseHovered == false) )
            {
                isHovered = false;
                isClicked = false;
                isAltClicked = false;
                display();
                ret = this->unhoveredHandler();
            }
            else if( (isHovered == false) && (mouseHovered == true) )
            {
                isHovered = true;
                display();
                ret = this->hoveredHandler();
            }
            break;
    }

    return ret;
}

