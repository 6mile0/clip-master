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

    formed = False  # インスタンス変数ではなくクラス変数として定義



    def __init__(self):

        self.file_path = "./test.txt"



    def save_content_to_file(self, content):

        if ClipboardContentManager.formed != True:  # クラス名を使用してアクセス

            with open(self.file_path, 'w+') as file:

                file.write(content)

            ClipboardContentManager.formed = True  # クラス名を使用してアクセス



    def get_content_from_file(self):

        if os.path.exists(self.file_path) and ClipboardContentManager.formed:  # クラス名を使用してアクセス

            with open(self.file_path, 'r') as file:

                return file.read()

        return ""



    def clear_file(self):

        if os.path.exists(self.file_path):

            os.remove(self.file_path)

            ClipboardContentManager.formed = False  # クラス名を使用してアクセス



def check_clipboard(windowTitle):
    WHITELIST_TITLES = ["Discord"]
    clipboard_manager = ClipboardContentManager()
    if sys.platform == "win32":
        windowTitle = windowTitle.split("-")[-1].strip()
    elif sys.platform == "darwin":
        windowTitle = windowTitle.split("-")[0].strip()
    
    # original_clipboard_contents変数をここで初期化します。
    original_clipboard_contents = pyperclip.paste()  # クリップボードの元の内容を保持
    
    if ClipboardContentManager.formed != True:
        clipboard_manager.save_content_to_file(original_clipboard_contents)  # 一時ファイルに保存
        ClipboardContentManager.formed = True

    if windowTitle in WHITELIST_TITLES:
        print(original_clipboard_contents)
        # 保存された一時ファイルのパスを取得してアップロードする
        file_path = clipboard_manager.file_path
        url = upload_file(file_path)
        pyperclip.copy(url)
    else:
        print(original_clipboard_contents)
        # 必要なら、一時ファイルから内容を復元して再度クリップボードにコピーする
        restored_content = clipboard_manager.get_content_from_file()
        pyperclip.copy(restored_content)
        clipboard_manager.clear_file() #のコメントアウトが解除されていないため、不要な行は削除または正しいメソッド名に修正してください。




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