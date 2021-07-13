import os.path

class BrowseFiles:
    pass


# def print_dir(path):
#     num = 1
#     folders = []
#     files = []
#     all_files = os.listdir(path)
#     for file in all_files:
#         if os.path.isdir(os.path.join(path, file)):
#             folders.append(str(num) + " - " + file)
#             num += 1
#         else:
#             files.append(file)
#
#     print('files:\n')
#     for file in files:
#         print(file)
#     print('\n')
#     print('folders:\n')
#     for folder in folders:
#         print(folder)
#     print('\n')
#
#     choice = int(input('Type the number of the folder you want to look in: '))
#
#     return folders, files, choice, path
#
#
# path = 'C:\\'
# my_folders, my_files, my_choice, my_path = print_dir(path)
#
# # a = my_chosen_file - 1
# # b = my_folders[a]
# # c = b[b.index('-')+2::]
# # d = os.path.join(path, c)
# # print_dir(d)
#
# list_location = my_folders[my_choice - 1]
# test = os.path.join(path, list_location[list_location.index('-') + 2::])
#
# print_dir(os.path.join(my_path, list_location[list_location.index('-') + 2::]))
