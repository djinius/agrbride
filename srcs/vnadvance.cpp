#include "vnadvance.h"
#include "common.h"

vnAdvanceLayer::vnAdvanceLayer(Window* window):
    mNameText(window, "", SDL_Color{255, 255, 0}), mDialogueText(window, "")
{
    addUpperDisplayable(&mNameText);
    addUpperDisplayable(&mDialogueText);
    mNameText.moveTo(960, 900, .5, .5);
    mDialogueText.moveTo(960, 960, .5, .5);
}

bool vnAdvanceLayer::handleEvent(const SDL_Event* event)
{
    bool ret = Layer::handleEvent(event);

    for (const auto displayable : mUpperDisplayables)
    {
        TRACE( "Upper display %p\n", displayable );
        displayable->display();
    }

    if(!ret)
    {
        switch(event->type)
        {
            case SDL_MOUSEBUTTONDOWN:
                advance();
                ret = true;
                break;
            default:
                break;
        }
    }

    return ret;
}

void vnAdvanceLayer::appendDialogues(vnDialogue* dialogues, int size)
{
    int i;

    for(i = 0; i < size; i++)
    {
        mDialogues.push_back(&dialogues[i]);
    }
}

void vnAdvanceLayer::purgeDialogues()
{
    mDialogues.clear();
    mCurrentDialogue = mDialogues.begin();
    mNameText.update("");
    mDialogueText.update("");
}

void vnAdvanceLayer::begin()
{
    mCurrentDialogue = mDialogues.begin();
    mNameText.update((*mCurrentDialogue)->mSayer);
    mDialogueText.update((*mCurrentDialogue)->mDialogue);
}

void vnAdvanceLayer::advance()
{
    if( mCurrentDialogue == mDialogues.end() )
    {
        mNameText.update("");
        mDialogueText.update("");
    }
    else
    {
        mCurrentDialogue++;
        if( mCurrentDialogue == mDialogues.end() )
        {
            mNameText.update("");
            mDialogueText.update("");
        }
        else
        {
            mNameText.update((*mCurrentDialogue)->mSayer);
            mDialogueText.update((*mCurrentDialogue)->mDialogue);
        }
    }
}

void vnAdvanceLayer::display()
{

}
