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

class QuitButton: public Button
{
	public:
		QuitButton(Application* App): Button(App->getWindowSurface()), mApp{App} {}
		virtual bool releasedHandler() { return true; }
		virtual bool altReleasedHandler() { mApp->quit(); return true; }

	private:
		Application* mApp;
};

#if defined(WIN32)
int WinMain( int argc, char* args[] )
#else
int main( int argc, char* args[] )
#endif
{
	//Start up SDL and create window
	bool quit = false;
	char* path = (char*)"./images/00291-386992299.png";
	SDL_Event event;
	Window gameWindow("신이 다스리는 농원");
	Layer UI;
	Layer World;
	Application app(&gameWindow);
	QuitButton exampleButton(&app);

	UI.subscribe(&exampleButton);

	if( argc == 2 )
	{
		path = args[1];
	}
	else
	{
		printf("Using default path: %s\n", path);
	}

	while( !quit )
	{
		while( SDL_PollEvent(&event) != 0 )
		{
			if( (event.type == SDL_QUIT) || ( (event.type == SDL_KEYDOWN) && (event.key.keysym.sym == SDLK_ESCAPE) ) )
			{
				quit = true;
			}
			else
			{
				if( UI.handleEvent(&event) )
				{
					gameWindow.renderFrame();
					continue;
				}
				else if( World.handleEvent(&event) )
				{
					gameWindow.renderFrame();
					continue;
				}
			}

			gameWindow.renderFrame();
		}
	}

	return 0;
}
