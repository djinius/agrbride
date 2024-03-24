/*This source code copyrighted by Lazy Foo' Productions 2004-2024
and may not be redistributed without written permission.*/

//Using SDL, SDL_image, standard IO, and strings
#include <SDL.h>
#include <SDL_image.h>
#include <stdio.h>
#include <string>
#include "common.h"
#include "base.h"
#include "button.h"
#include "text.h"
#include "keyhandler.h"
#include "image.h"
#include "vnadvance.h"

#if 0
class QuitButton: public Button
{
	public:
		QuitButton(Application* App, SDL_Rect rect): Button(App->getRenderer(), rect), mApp{App} {}
		virtual bool releasedHandler() { mApp->quit(); return true; }
		virtual bool altReleasedHandler() { return true; }

	private:
		Application* mApp;
};
#endif

class ImageMoveHandler: public Image, public KeyHandler
{
	public:
		ImageMoveHandler(Window* window): Image(window) {}
		virtual bool keyPressed(const int keyCode, const bool pressed)
		{
			TRACE("Key code [%d]: %s\n", keyCode, pressed? "PRESSED":"RELEASED");
			if(!pressed)
			{
				switch( keyCode )
				{
					case SDLK_UP:
						mYPos -= 10;
						break;
					case SDLK_DOWN:
						mYPos += 10;
						break;
					case SDLK_LEFT:
						mXPos -= 10;
						break;
					case SDLK_RIGHT:
						mXPos += 10;
						break;
				}
			}

			return false;
		}
};

#if defined(WIN32)
int WinMain( int argc, char* args[] )
#else
int main( int argc, char* args[] )
#endif
{
	Application::initializeStatic();

	//Start up SDL and create window
	bool quit = false;
	SDL_Event event;
	Window gameWindow("신이 다스리는 농원");
	vnAdvanceLayer UI(&gameWindow);
	// Application app(&gameWindow);
	// QuitButton exampleButton(&app);
	// Text exampleText(&gameWindow, "Hello, SDL World! -> 하늘에서 우주선이 내려옵니다.");
	ImageMoveHandler exampleImage(&gameWindow);

	void appendExampleDialogues(vnAdvanceLayer&);
	
	exampleImage.loadImage("./images/backgrounds/field.png");
	// exampleText.moveTo(960, 960, .5, .5);

	// UI.subscribe(&exampleButton);
	UI.subscribe(&exampleImage);
	UI.addDisplayable(&exampleImage);

	appendExampleDialogues(UI);
	UI.begin();

	while( !quit )
	{
		while( SDL_PollEvent(&event) != 0 )
		{
			gameWindow.beginRender();

			if( (event.type == SDL_QUIT) || ( (event.type == SDL_KEYDOWN) && (event.key.keysym.sym == SDLK_ESCAPE) ) )
			{
				quit = true;
			}
			else
			{
				UI.handleEvent(&event);
			}

			gameWindow.finishRender();
		}
	}

	return 0;
}
