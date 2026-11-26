import os

folder_path = r"D:\Duckcreek\Queries"

print("Folder exists:", os.path.exists(folder_path))

print("Is directory:", os.path.isdir(folder_path))

print("\nFiles available:")

for root, dirs, files in os.walk(folder_path):

    for file in files:

        print(file)