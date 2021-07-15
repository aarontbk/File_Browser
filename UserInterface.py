import Directory
import File


class UserInterface:
    def __init__(self, path):
        self.path = path

    def start(self):
        ans: str = input("What do you want to do: ")
        while ans.lower() != "quit":
            if ans.lower() == "dir":
                d = Directory.Directory(self.path)
                print(d.print_items)
                # f = File.File(self.path)
                # print(f.__str__())
            ans = input("What do you want to do: ")