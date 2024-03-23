#include "base.h"
#include "common.h"
#include <assert.h>

using namespace std;

Font* Font::mDefaultFont = nullptr;

Font::Font(const string& fontPath, const int fontSize)
{
    TRY_RAISE( (mFont = TTF_OpenFont(fontPath.c_str(), fontSize)) != NULL, EOPENFONT );
    TRACE("Font '%s' loaded successfully.\n", fontPath.c_str());
    mIsLoaded = true;

    CATCH(EOPENFONT)
    TRACE("Error opening font: '%s'\n", fontPath.c_str());
    mFont = *getDefaultFont();
    mIsLoaded = false;

    FINALLY;
}

Font::~Font()
{
    if( mIsLoaded )
    {
        TTF_CloseFont(mFont);
    }
}

int Font::initializeStatic(void)
{
    int resultCode;
    resultCode = TTF_Init();
    TRY( resultCode >= 0 );
    Font::mDefaultFont = new Font("./fonts/d2coding_ligature.ttf", 32);
    assert( Font::mDefaultFont->isLoaded() == true );

    return 0;

    FINALLY;
    return resultCode;
}

void Font::destroyStatic(void)
{
    TTF_Quit();
}
