import os

import Directory


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
                d, folders, files = Directory.Directory(path).print_items()
                print(d)

            elif ans == "path":
                print(self.print_path(path))

            elif ans in folders:
                path = os.path.join(path, ans)
                d, folders, files = Directory.Directory(path).print_items()
                print(d)

            elif ans.split(" ")[0] == "rename" and ans.split(" ")[1] in files:
                old_name = os.path.join(path, ans.split(" ")[1])
                new_name = os.path.join(path, input("New file name: "))
                print(self.rename(old_name, new_name))

            elif ans.split(" ")[0] == "delete" and ans.split(" ")[1] in files:
                print(self.delete(os.path.join(path, ans.split(" ")[1])))

            elif ans.split(" ")[0] == "copy" and ans.split(" ")[1] in files:
                print(self.copy(os.path.join(path, ans.split(" ")[1]), os.path.join(path, input("New file name: "))))
            ans = input(que)


    def print_path(self, path):
        return path

    def rename(self, old_name, new_name):
        os.rename(old_name, new_name)
        return f"Renamed {old_name} as: {new_name}"

    def delete(self, name):
        os.remove(name)
        return f"Deleted: {name}"

    def copy(self, name, new_name):
        file = open(name, "r")
        file_content = file.read()
        file.close()

        new_file = open(new_name, "w")
        new_file.write(file_content)
        new_file.close()

        return f"Copied {name} to new file: {new_name}"

