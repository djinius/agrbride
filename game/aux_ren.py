"""renpy
init -1 python:
"""

class MyScreenshot(Action, DictEquality):
    """
        :doc: file_action

        Saves the file.

        The button with this slot is selected if it's marked as the
        newest save file.

        """

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

