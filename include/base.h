#pragma once

#include <string>
#include <vector>
#include <algorithm>
#include <SDL.h>
#include <SDL_image.h>
#include <SDL_ttf.h>

class Application
{
    public:
        Application() {}
        ~Application() {}

        int initialize(const int = IMG_INIT_JPG | IMG_INIT_PNG);
        void finalize();

        // SDL_Renderer* getRenderer() { return mWindow->getMainRenderer(); }
        void quit() { SDL_Event QuitEvent { SDL_QUIT }; SDL_PushEvent(&QuitEvent); }

    public:
        static int initializeStatic(const int = IMG_INIT_JPG | IMG_INIT_PNG);
        static void destroyStatic();
        static Application& getApplication() {return gApplication;}

    private:
        static Application gApplication;
};

class Window
{
    public:
        Window(const std::string&);
        ~Window();
        void beginRender();
        void finishRender();
        SDL_Renderer* getRenderer() { return mSDLRenderer; }

    private:
        int init(const std::string&);
        SDL_Window* mSDLWindow { nullptr };
        SDL_Renderer* mSDLRenderer { nullptr };
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
        Displayable(SDL_Renderer* renderer):
            mSDLRenderer(renderer),
            mW(0), mH(0), mXPos(0), mYPos(0), mXAnchor(0.), mYAnchor(0.)
            {}
        Displayable(Window* window): Displayable(window->getRenderer()) {}
        virtual ~Displayable() { destroyTexture(); }
        virtual void display();
        void moveTo(const int, const int, const double, const double);

    protected:
        /* SDL displayable functions */
        SDL_Texture* createTexture(SDL_Surface* surface) { return (mTexture = SDL_CreateTextureFromSurface(mSDLRenderer, surface)); }
        void destroyTexture(void) { if( mTexture != nullptr) SDL_DestroyTexture(mTexture); mTexture = nullptr; }
        
        void setColorKey(SDL_Surface* surface, int flags, unsigned int key) { SDL_SetColorKey(surface, flags, key); }
        void freeSurface(SDL_Surface* surface) { if(surface != nullptr) SDL_FreeSurface(surface); }
        const char* getError() { return SDL_GetError(); }

    protected:
        SDL_Texture* mTexture {nullptr};
        SDL_Renderer* mSDLRenderer { nullptr };

        void            setSize(SDL_Surface* surface) {setSize(surface->w, surface->h);}
        void            setSize(const int w, const int h) {mW = w; mH = h;}
        SDL_Rect        calcXYPos();
        int             mW, mH;
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
