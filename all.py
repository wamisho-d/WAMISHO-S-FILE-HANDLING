import os
def list_directory_contents(path):
    if not os.path.exists(path):
        print(f"The path '{path} does not exist.")
        return
    if not os.path.isdir(path):
     print(f"The path '{path}' is not directory.")
     return
    contents = os.listdir(path)
    if not contents:
       print(f"The directory '{path}' is empty.")
    else:
       print(f"Contents of the directory'{path}':")
       for item in contents:
          print(item)
directory_path = input("please enter the directory path:")
list_directory_contents(directory_path)
