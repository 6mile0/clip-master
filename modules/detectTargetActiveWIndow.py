import sys

# Active window title detection
def getActiveWindowTitle() -> str:
    activeWindowTitle = ""

    # For Mac OS X
    if sys.platform == "darwin":
        from AppKit import NSWorkspace
        from Quartz import (
            CGWindowListCopyWindowInfo,
            kCGWindowListOptionOnScreenOnly,
            kCGNullWindowID
        )

        curr_pid = NSWorkspace.sharedWorkspace().activeApplication()[
            'NSApplicationProcessIdentifier']
        options = kCGWindowListOptionOnScreenOnly
        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

        for window in windowList:
            pid = window['kCGWindowOwnerPID']
            ownerName = window['kCGWindowOwnerName']

            if curr_pid == pid:
                activeWindowTitle = ownerName

    # For Windows
    elif sys.platform == "win32":
        import win32gui

        activeWindowTitle = win32gui.GetWindowText(
            win32gui.GetForegroundWindow())

    else:
        pass

    return activeWindowTitle
