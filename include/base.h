#pragma once

#include <string>
#include <vector>
#include <algorithm>
#include <SDL.h>
#include <SDL_ttf.h>

class Window
{
    public:
        Window(const std::string&);
        ~Window();
        void beginRender();
        void finishRender();
        SDL_Surface* getSurface() { return mSDLWindowSurface; }
        SDL_Renderer* getRenderer() { return mSDLRenderer; }

    private:
        int init(const std::string&);
        SDL_Window* mSDLWindow { nullptr };
        SDL_Renderer* mSDLRenderer { nullptr };
        SDL_Surface* mSDLWindowSurface { nullptr };
};

class EventReceiver
{
    public:
        EventReceiver(): mIsHovered(false), mIsClicked(false), mIsAltClicked(false), mIsSelected(false) {}
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

        virtual bool getHovered() { return mIsHovered; }
        virtual bool setHovered(bool isHovered = true) { return (mIsHovered = isHovered); }
        virtual bool getClicked() { return mIsClicked; }
        virtual bool setClicked(bool isClicked = true) { return (mIsClicked = isClicked); }
        virtual bool getAltClicked() { return mIsAltClicked; }
        virtual bool setAltClicked(bool isAltClicked = true) { return (mIsAltClicked = isAltClicked); }
        virtual bool getSelected() { return mIsSelected; }
        virtual bool setSelected(bool isSelected = true) { return (mIsSelected = isSelected); }
        virtual bool getSensitive() { return mIsSensitive; }
        virtual bool setSensitive(bool isSensitive = true) { return (mIsSensitive = isSensitive); }

    private:
         bool mIsHovered;
         bool mIsClicked;
         bool mIsAltClicked;
         bool mIsSelected;
         bool mIsSensitive;
};

class Displayable
{
    public:
        Displayable(SDL_Surface* surface = nullptr, SDL_Renderer* renderer = nullptr):
            mSDLWindowSurface(surface), mSDLRenderer(renderer),
            mXPos(0), mYPos(0), mXAnchor(0.), mYAnchor(0.)            
            {}
        Displayable(Window* window): Displayable(window->getSurface(), window->getRenderer()) {}
        virtual void display() = 0;
        void moveTo(const int, const int, const double, const double);

    protected:
        int blitSurface(SDL_Surface* srcSurface, const SDL_Rect* srcRect, SDL_Rect* dstRect) { return SDL_BlitSurface(srcSurface, srcRect, mSDLWindowSurface, dstRect); }
        SDL_Surface* convertSurface(SDL_Surface* srcSurface) { return SDL_ConvertSurface(srcSurface, mSDLWindowSurface->format, 0); }
        SDL_Surface* mSDLWindowSurface {nullptr};
        SDL_Renderer* mSDLRenderer { nullptr };

        SDL_Rect        calcXYPos(SDL_Surface*);
        int             mXPos, mYPos;
        double          mXAnchor, mYAnchor;
};

class Layer
{
    public:
        virtual bool handleEvent(const SDL_Event* event);
        void subscribe(EventReceiver* receiver) { mSubscribers.push_back(receiver); }
        void addDisplayable(Displayable* displayable) { mDisplayables.push_back(displayable); }
        void removeDisplayable(Displayable* displayable) { remove(mDisplayables.begin(), mDisplayables.end(), displayable); }

    private:
        std::vector<EventReceiver*> mSubscribers;
        std::vector<Displayable*> mDisplayables;
};

class Font
{
    public:
        Font(const std::string&, const int);
        virtual ~Font();
        operator TTF_Font*() {return mFont;}
        bool isLoaded() {return mIsLoaded;}

        static int initializeStatic(void);
        static void destroyStatic(void);
        static Font* getDefaultFont() { return mDefaultFont; }

    private:
        TTF_Font* mFont;
        bool mIsLoaded;

        static Font* mDefaultFont;
};

class Application
{
    public:
        Application(Window* Window) : mWindow { Window } {}
        SDL_Surface* getWindowSurface() { return mWindow->getSurface(); }
        SDL_Renderer* getRenderer() { return mWindow->getRenderer(); }
        void quit() { SDL_Event QuitEvent { SDL_QUIT }; SDL_PushEvent(&QuitEvent); }

    private:
        Window* mWindow;
};
