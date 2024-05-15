import sys

import pyperclip

import os



# Mac用

if sys.platform == "darwin":

    from AppKit import NSWorkspace

    from Quartz import (

        CGWindowListCopyWindowInfo,

        kCGWindowListOptionOnScreenOnly,

        kCGNullWindowID

    )



    def getActiveWindowTitle():

        curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()

        curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']

        curr_app_name = curr_app.localizedName()

        options = kCGWindowListOptionOnScreenOnly

        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)



        for window in windowList:

            pid = window['kCGWindowOwnerPID']

            if curr_pid == pid:

                ownerName = window['kCGWindowOwnerName']

                windowTitle = window.get('kCGWindowName', u'Unknown')

                return ownerName + " - " + windowTitle



        return ""



# Windows用

elif sys.platform == "win32":

    import win32gui



    def getActiveWindowTitle():

        return win32gui.GetWindowText(win32gui.GetForegroundWindow())



else:

    def getActiveWindowTitle():

        return ""



def upload_file(file_path):

    # ここにファイルをアップロードするためのコードを実装する

    return "http://example.com/uploaded_file.txt"



class ClipboardContentManager:

    formed = False



    def __init__(self):

        self.file_path = "./test.txt"



    def save_content_to_file(self, content):

        if ClipboardContentManager.formed != True:

            with open(self.file_path, 'w+') as file:

                file.write(content)

            ClipboardContentManager.formed = True



    def get_content_from_file(self):

        if os.path.exists(self.file_path) and ClipboardContentManager.formed:

            with open(self.file_path, 'r') as file:

                return file.read()

        return ""



    def clear_file(self):

        if os.path.exists(self.file_path):

            os.remove(self.file_path)

            ClipboardContentManager.formed = False



def check_clipboard(windowTitle):
    WHITELIST_TITLES = ["Discord"]
    clipboard_manager = ClipboardContentManager()
    windowTitle = windowTitle.split("-")[-1].strip()
    
    original_clipboard_contents = pyperclip.paste()
    
    if ClipboardContentManager.formed != True:
        clipboard_manager.save_content_to_file(original_clipboard_contents)
        ClipboardContentManager.formed = True

    if windowTitle in WHITELIST_TITLES:
        print(original_clipboard_contents)
        file_path = clipboard_manager.file_path
        url = upload_file(file_path)
        pyperclip.copy(url)
    else:
        print(original_clipboard_contents)
        restored_content = clipboard_manager.get_content_from_file()
        pyperclip.copy(restored_content)
        clipboard_manager.clear_file()




def main():

    bufWindowTitle = ""

    try:

        while True:

            activeWindowTitle = getActiveWindowTitle()

            if bufWindowTitle != activeWindowTitle:

                check_clipboard(activeWindowTitle)

                bufWindowTitle = activeWindowTitle

    except KeyboardInterrupt:

        sys.exit(0)



if __name__ == '__main__':

    main()