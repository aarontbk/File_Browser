import create_file, open_file, browse_files
import os.path

path = "C:\\"
num = 1
folders = []
files = []
all_files = os.listdir(path)
for file in all_files:
    if os.path.isdir(os.path.join(path, file)):
        folders.append(str(num) + " - " + file)
        num += 1
    else:
        files.append(file)

print('files:\n')
for file in files:
    print(file)
print('\n')
print('folders:\n')
for folder in folders:
    print(folder)
print('\n')

try:
    ans = int(input("1 - create a file, 2 - open a file, 3 - browse files: "))
except:
    print("Invalid answer")
    quit()

if ans == 1:
    name = input("file name: ")
    content = input("file content: ")
    create_file.CreateFile(name, content)
elif ans == 2:
    name = input("file name: ")
    open_file.OpenFile(name)
elif ans == 3:
    browse_files.BrowseFiles()
else:
    print(f"there is no choice: {ans}")
