import os

import Directory


# support following options:
# copy file: file_name, new_file_name
# delete file: file_name
# rename file: file_name, new_file_name
#

class UserInterface:
    def __init__(self, path):
        self.path = path

    def start(self):
        que: str = "What do you want to do: "
        ans: str = input(que)
        self.usage(que, ans)

    def usage(self, que, ans):
        while ans.lower() != "quit":
            if ans == "dir":
                path = self.path
                d, f = Directory.Directory(path).print_items()
                print(d)
            elif ans == "path":
                print(self.print_path(path))
            elif ans in f:
                path = os.path.join(path, ans)
                d, f = Directory.Directory(path).print_items()
                print(d)
            ans = input(que)

    def print_path(self, path):
        return path
