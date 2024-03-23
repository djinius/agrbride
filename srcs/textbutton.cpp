#include "textbutton.h"
#include "common.h"

void TextButton::display()
{
    auto [r, g, b, a] { isClicked? ClickedColor: isAltClicked? AltClickedColor: isHovered? HoverColor : BGColor };
    TRACE("Button color code: %d %d %d %d\n", r, g, b, a);
    SDL_FillRect(mSDLWindowSurface, &Rect, SDL_MapRGB(mSDLWindowSurface->format, r, g, b));
}
