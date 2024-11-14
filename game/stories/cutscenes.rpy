
label playCutScene(cutSceneObject):

    scene black with dissolve
    pause 1.

    call expression cutSceneObject.getLabelName()
    $ cutSceneObject.finish()
    $ nextCutScene = None

    scene black with dissolve

    return

