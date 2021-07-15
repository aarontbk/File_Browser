import os
import File


class Directory:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path[:-2:])
        self.creation_date = os.path.getctime(path)

    def __str__(self):
        return f"Name: {self.name}, creation date: {self.creation_date}"

    @property
    def print_items(self) -> str:
        num: int = 1
        folders = []
        files = []
        all_files = os.listdir(self.path)
        for file in all_files:
            if os.path.isdir(os.path.join(self.path, file)):
                folders.append(str(num) + " - " + file)
                num += 1
            else:
                f1 = File.File(os.path.join(self.path, file))
                files.append(f1.__str__)

        return f'Files:\n{[file for file in files]}\nFolders:\n{[folder for folder in folders]}\n'
