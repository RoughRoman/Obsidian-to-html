import os
from multiprocessing import Pool
from shutil import copy

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
                html_strs = p.map(format, self.md_files)

            #for str in html_strs:

        else:
            print("single")
            # process with single cpu
            for md_file in self.md_files:
                print(format(md_file))

        # copy images into dest folder in its own subfolder
        image_dest_folder = os.path.join(self.dest_folder, "Images")
        os.mkdir(image_dest_folder)

        for img_file in self.images:
            copy(img_file, image_dest_folder, True)
        
    def traverse(self):
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                     self.md_files.append(os.path.join(root, file))
                elif file.endswith(".png"):
                    self.images.append(os.path.join(root, file))


    def format(self, md_filePath):
        md_file = open(md_filePath,"r")
        md_str = md_file.read()
        md_file.close()

        html_file = (
            f'<!DOCTYPE html>'+ '\n'+
            '<html lang="en">'+ '\n'+
                '<head>'+ '\n'+
                    '<meta charset="UTF-8">'+ '\n'+
                    '<meta name="viewport" content="width=device-width, initial-scale=1.0">'+ '\n'+
                    '<meta http-equiv="X-UA-Compatible" content="ie=edge">'+ '\n'+
                    '<title>{title}</title>'+ '\n'+
                    '<link rel="stylesheet" href="style.css">'+ '\n'+
                '</head>'+ '\n'+
                '<body>'+ '\n'+
                    '<script src="index.js"></script>'+ '\n'+
                    
                '</body>'+ '\n'+
            '</html>'
            ) 
