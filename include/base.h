#pragma once

#include <string>
#include <vector>
#include <SDL.h>

class EventReceiver
{
    public:
        virtual bool handleEvent(const SDL_Event* event) = 0;

        /* 마우스 오버시 */
        virtual bool hoveredHandler() {return false;}
        /* 마우스 오버 종료 */
        virtual bool unhoveredHandler() {return false;}
        /* 마우스 왼쪽 클릭 */
        virtual bool clickedHandler() {return false;}
        /* 마우스 왼쪽 놓음 */
        virtual bool releasedHandler() {return false;}
        /* 마우스 오른쪽 클릭 */
        virtual bool altClickedHandler() {return false;}
        /* 마우스 오른쪽 놓음 */
        virtual bool altReleasedHandler() {return false;}
        /* 키보드 누름 */
        virtual bool keyPressed(const int, const bool) {return false;}
        /* 키보드 놓음 */
        virtual bool keyReleased(const int, const bool) {return false;}

    protected:
        bool isHovered;
        bool isClicked;
        bool isAltClicked;
};

class Displayable
{
    public:
        Displayable(SDL_Surface* surface = nullptr): mSDLWindowSurface(surface) {}
        virtual void display() = 0;

    protected:
        SDL_Surface* mSDLWindowSurface {nullptr};
};

class Layer
{
    public:
        virtual bool handleEvent(const SDL_Event* event)
        {
            for (const auto handler : mSubscribers)
            {
                if( handler->handleEvent(event) ) { return true; }
            }
            return false;
        }
        void subscribe(EventReceiver* receiver) { mSubscribers.push_back(receiver); }

    private:
        std::vector<EventReceiver*> mSubscribers;
        std::vector<Displayable*> mDisplayables;
};

class Window
{
    public:
        Window(const std::string&);
        ~Window() {}
        void renderFrame();
        SDL_Surface* getSurface() { return mSDLWindowSurface; }

    private:
        int init(const std::string&);
        SDL_Window* mSDLWindow { nullptr };
        SDL_Surface* mSDLWindowSurface { nullptr };
};

class Application
{
    public:
        Application(Window* Window) : mWindow { Window } {}
        SDL_Surface* getWindowSurface() { return mWindow->getSurface(); }
        void quit() { SDL_Event QuitEvent { SDL_QUIT }; SDL_PushEvent(&QuitEvent); }

    private:
        Window* mWindow;
};
