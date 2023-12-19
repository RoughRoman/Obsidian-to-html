import os
from multiprocessing import Pool
from shutil import copy
import re
import platform
from template import html_template

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

        # copy images into dest folder in its own subfolder
        image_dest_folder = os.path.join(self.dest_folder, "Images")

        # create the folder if it does not already exist
        if not os.path.isdir(image_dest_folder):
            os.mkdir(image_dest_folder)

        for img_file in self.images:
            if platform.system() == "Windows":
                copy(img_file, image_dest_folder)
            else:
                copy(img_file, image_dest_folder, True)
            

        # create sub folder for html files if it does not already exist
        notes_dest_folder = os.path.join(self.dest_folder,"Notes")
        if not os.path.isdir(notes_dest_folder):
            os.mkdir(notes_dest_folder)

        # Process the Files
        if parallel:
            with Pool() as p:
                p.map(self.format, self.md_files)
        else:
            for md_file in self.md_files:
                self.format(md_file)

        self.createIndex()


    def traverse(self):
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                     self.md_files.append(os.path.join(root, file))
                elif file.endswith(".png"):
                    self.images.append(os.path.join(root, file))


    def format(self, md_filePath):
        title = os.path.basename(md_filePath).split(".")[0]
        html_dir = os.path.join(self.dest_folder,"Notes",f"{title}.html")
        html_file = open(html_dir,"w")
        html_content = ""

        # obtain a file handle
        with open(md_filePath,"r") as md_file:
 
            for line in md_file:
                line = self.formatLine(line,r"\[\[.+?\]\]")
                html_content += line

        html_file.write(html_template.format(title, html_content))
            
        html_file.close()

    def formatLine(self, line, regexp):
        # Works well. Lets hope someone doesnt end a name of an md file with .png
        while( re.search(regexp, line) != None):
            image_match = re.search(regexp, line)
            match_pos = image_match.span()
            tag_content = line[match_pos[0] + 2 : match_pos[1] - 2]
            print(tag_content)
            if tag_content.endswith(".png"):

                tag = f'<img src = "{os.path.join("..\Images",tag_content)}"></img>'
                line = line[:match_pos[0]-1] + tag + line[match_pos[1]:]
                # The -1 to the start index is to nab the ! from image tags
            else:
                print(os.path.join("Notes",tag_content + ".html"))
                tag = f'<a href = "{tag_content + ".html"}">{tag_content}</a>'
                line = line[:match_pos[0]]+ tag + line[match_pos[1]:]
            
            
        return line
    
    def createIndex(self):

        index_dir = os.path.join(self.dest_folder,"Note-Index.html")
        index_file = open(index_dir,"w")
        index_file.write(f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Note Index</title>
    </head>
    <body>
        <ul>""")

        for file in self.md_files:
            file_name = os.path.basename(file).split(".")[0]
            index_file.write(f'<li><a href = "Notes\{file_name}.html" >{file_name}</a></li>')

        index_file.write(f"""</ul>
    </body>
</html>""")
            
        index_file.close()
        
        




