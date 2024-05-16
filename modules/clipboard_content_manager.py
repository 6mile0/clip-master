import os
class ClipboardContentManager:
    file_path = "./test.txt"

    @classmethod
    def save_content_to_file(cls, content):
        with open(cls.file_path, 'w+') as file:
            file.write(content)

    @classmethod
    def get_content_from_file(cls):
        if os.path.exists(cls.file_path):
            with open(cls.file_path, 'r') as file:
                return file.read()
        return ""

    @classmethod
    def clear_file(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
    @classmethod
    def exists_clipboard_contents(cls):
        return os.path.exists(cls.file_path)