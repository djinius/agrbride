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
        void begin();
        void advance();
        void display();

    protected:
        Text mNameText;
        Text mDialogueText;

    private:
        std::vector<vnDialogue*> mDialogues;
        std::vector<vnDialogue*>::iterator mCurrentDialogue;
};
