import os
import shutil

from_dir = "C:/Users/terri/Downloads"
to_dir = "C:/Users/terri/Desktop/The Stuff/Farid's stuff/Coding/BYJU's downloads/Projects/Document_files"

list_of_files = os.listdir(from_dir)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    print(name)
    print(extension)

#print(list_of_files)