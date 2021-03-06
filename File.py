import os


class File:
    def __init__(self, path):
        self.name = os.path.basename(path)
        self.creation_date = os.path.getctime(path)
        self.size = os.path.getsize(path)

    def __str__(self):
        return f"Name: {self.name}, creation date: {self.creation_date}, size: {self.size}"