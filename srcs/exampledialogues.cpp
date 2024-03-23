#include "vnadvance.h"

vnDialogue exampleDialogue[] = 
{
    {"만다", "나 예뻐?"},
    {"만다", "읍내로 놀러 나가자."},
    {"만다", "고기 사줘!"},
    {"만다", "맛있다."}
};

void appendExampleDialogues(vnAdvanceLayer& layer)
{
    layer.appendDialogues(exampleDialogue, sizeof(exampleDialogue)/sizeof(vnDialogue));
}