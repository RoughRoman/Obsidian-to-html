import os

class Converter:
    def __init__(self, vault):
        self.md_files = []
        self.images = []
        self.vault_path = vault
        self.output_folder = ""

    def parseFile(self):
        # simply collect all of the files up into the respective lists.
        traverse(self.vault_path, self.md_files, self.images)
        print("MD files: ")
        print(self.md_files)
        print("\n")
        print("Image files: ")
        print(self.images)

    def convert(self, file_list, parallel = False):
        # process a list of files. 
        pass

def traverse(folder_path, image_list, md_list):
    # recurse through the files and append to lists 
    print("start Traverse")
    for file in os.listdir(folder_path):
        print(file)
        if file.endswith('.md'):
            md_list.append(file)

        elif file.endswith(".png"):
            image_list.append(file)

        elif os.path.isdir(file):
            print("isDir")
            traverse(file, md_list, image_list )
        
        else:
            continue
