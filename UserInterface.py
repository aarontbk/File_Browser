import Directory


class UserInterface:
    def __init__(self, path):
        self.path = path

    def start(self):
        ans: str = input("What do you want to do: ")
        while ans.lower() != "quit":
            if ans.lower() == "dir":
                d = Directory.Directory(self.path)
                print(d.print_items)
            ans = input("What do you want to do: ")