import os

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