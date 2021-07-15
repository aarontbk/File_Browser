def create_file(name, content):
    with open(name, "x") as f:
        f.write(content)
