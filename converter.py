import os
from multiprocessing import Pool
from markdown2 import markdown_path

class Converter:
    def __init__(self, vault_path, dest_folder):
        self.md_files = []
        self.images = []
        self.vault_path = vault_path
        self.dest_folder = dest_folder

    def parseFile(self, parallel = False):
        # simply collect all of the files up into the respective lists.
        self.traverse()
        self.convert(parallel)

    def convert(self, parallel):
        if parallel:
            # process in sub processes
            with Pool() as p:
                p.map(markdown_path, self.md_files)
            
        else:
            print("single")
            # process with single cpu
            for md_file in self.md_files:
                print(markdown_path(md_file))
            

    def traverse(self):
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                     self.md_files.append(os.path.join(root, file))
                elif file.endswith(".png"):
                    self.images.append(os.path.join(root, file))
