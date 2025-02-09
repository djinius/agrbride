"""renpy
init -1 python:
"""

class MyScreenshot(Action, DictEquality):
    alt = "Screenshot"

    def __init__(self):
        super(MyScreenshot, self).__init__()

    def __call__(self):
        import os.path
        import os
        import __main__

        dest = config.renpy_base

        if renpy.macapp:
            dest = os.path.expanduser(b"~/Desktop")

        pattern = renpy.store._screenshot_pattern or config.screenshot_pattern

        # Try to pick a filename.
        i = 1
        while True:
            fn = os.path.join(dest, pattern % i)
            if not os.path.exists(fn):
                break
            i += 1

        try:
            dn = os.path.dirname(fn)
            if not os.path.exists(dn):
                os.makedirs(dn)
        except Exception:
            pass

        try:
            if not renpy.screenshot(fn):
                renpy.notify(__("Failed to save screenshot as %s.") % fn)
                return

        except Exception:
            import traceback
            traceback.print_exc()
            renpy.notify(__("Failed to save screenshot as %s.") % fn)
            return

        renpy.hide_screen("screenshotScreen")
        renpy.sound.play("audio/ui/save.mp3", channel="sound3", loop=False)
        renpy.restart_interaction()
        renpy.show_screen("screenshotScreen")

class MyFileSave(FileSave):
    def get_sensitive(self):
        global _in_gameplay

        if _in_gameplay:
            return super(MyFileSave, self).get_sensitive()
        else:
            return False

class QuickNotify(Action):
    def predict(self):
        renpy.predict_screen("quickSaveNotify")

    def __call__(self):
        renpy.show_screen("quickSaveNotify")

def MyQuickSave(message=_("Quick save complete."), newest=False):
    """
    :doc: file_action

    Performs a quick save.

    `message`
        A message to display to the user when the quick save finishes.

    `newest`
        Set to true to mark the quicksave as the newest save.
        """

    rv = [ MyFileSave(1, page="quick", confirm=False, cycle=True, newest=newest, action=QuickNotify()) ]

    rv[0].alt = _("Quick save.")

    if not getattr(renpy.context(), "_menu", False):
        rv.insert(0, FileTakeScreenshot())

    return rv

