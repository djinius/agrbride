#pragma once

#include "base.h"
#include "text.h"

struct vnDialogue
{
    std::string mSayer;
    std::string mDialogue;
};

class vnAdvanceLayer: public Layer, public EventReceiver
{
    public:
        vnAdvanceLayer(Window*);
        virtual ~vnAdvanceLayer() {}

        virtual bool handleEvent(const SDL_Event*);

        void appendDialogues(vnDialogue*, int);
        void purgeDialogues();
        
        void begin();
        void advance();
        void display();

    protected:
        void addUpperDisplayable(Displayable* displayable) { mUpperDisplayables.push_back(displayable); }
        Text mNameText;
        Text mDialogueText;

    private:
        std::vector<vnDialogue*> mDialogues;
        std::vector<vnDialogue*>::iterator mCurrentDialogue;
        std::vector<Displayable*> mUpperDisplayables;
};
