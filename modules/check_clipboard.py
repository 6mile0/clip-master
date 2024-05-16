import pyperclip
from modules.clipboard_content_manager import ClipboardContentManager
import sys
from modules.upload_file import upload_file
def check_clipboard(windowTitle):
    WHITELIST_TITLES = ["Discord"]
    clipboard_manager = ClipboardContentManager()
    if sys.platform == "win32":
        windowTitle = windowTitle.split("-")[-1].strip()
    elif sys.platform == "darwin":
        windowTitle = windowTitle.split("-")[0].strip()

    original_clipboard_contents = pyperclip.paste()
    
    if ClipboardContentManager.formed != True:
        clipboard_manager.save_content_to_file(original_clipboard_contents)
        ClipboardContentManager.formed = True

    if windowTitle in WHITELIST_TITLES:
        file_path = clipboard_manager.file_path
        url = upload_file(file_path)
        pyperclip.copy(url)
    else:
        restored_content = clipboard_manager.get_content_from_file()
        pyperclip.copy(restored_content)
        clipboard_manager.clear_file()
        