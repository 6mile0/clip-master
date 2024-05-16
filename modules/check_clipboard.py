import pyperclip
from modules.clipboard_content_manager import ClipboardContentManager
import sys
import os
from modules.upload_file import upload_file
def check_clipboard(window_title):
    whitelist_titles = ["Discord"]
    platform = sys.platform
    title_key = -1 if platform == "win32" else 0
    window_title = window_title.split("-")[title_key].strip()

    original_clipboard_contents = pyperclip.paste()

    if not os.path.exists(ClipboardContentManager.file_path):
        ClipboardContentManager.save_content_to_file(original_clipboard_contents)

    if window_title in whitelist_titles:
        file_path = ClipboardContentManager.file_path
        url = upload_file(file_path)
        pyperclip.copy(url)
    else:
        restored_content = ClipboardContentManager.get_content_from_file()
        pyperclip.copy(restored_content)
        ClipboardContentManager.clear_file()
        