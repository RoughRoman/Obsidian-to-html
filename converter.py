import os
from multiprocessing import Pool
from shutil import copy
import re
import platform
from templates import html_template, css_template, index_template


class Converter:
    def __init__(self, vault_path, dest_folder):
        self.md_files = []
        self.images = []
        self.vault_path = vault_path
        self.dest_folder = dest_folder

    def convert(self, parallel):
        self.traverse()

        image_dest_folder = os.path.join(self.dest_folder, "Images")

        if not os.path.isdir(image_dest_folder):
            os.mkdir(image_dest_folder)

        for img_file in self.images:
            copy(img_file, image_dest_folder)
            
        notes_dest_folder = os.path.join(self.dest_folder,"Notes")
        if not os.path.isdir(notes_dest_folder):
            os.mkdir(notes_dest_folder)

        if parallel:
            with Pool() as p:
                p.map(self.generateHtml, self.md_files)
        else:
            for md_file in self.md_files:
                self.generateHtml(md_file)

        self.createIndex(index_template)

        self.createCssFile(css_template)

    def traverse(self):
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                     self.md_files.append(os.path.join(root, file))
                elif file.endswith(".png"):
                    self.images.append(os.path.join(root, file))


    def generateHtml(self, md_filePath):
        title = os.path.basename(md_filePath).split(".")[0]
        html_dir = os.path.join(self.dest_folder,"Notes",f"{title}.html")
        html_content = ""

        with open(md_filePath,"r") as md_file:
 
            for line in md_file:
                line = self.formatLine(line,r"\[\[.+?\]\]")
                html_content += line

        with open(html_dir,"w") as html_file:
            html_file.write(html_template.format(title, html_content))
            

    def formatLine(self, line, regexp):
        # Works well. Lets hope someone doesnt end a name of an md file with .png
        while( re.search(regexp, line) != None):
            image_match = re.search(regexp, line)
            match_pos = image_match.span()
            tag_content = line[match_pos[0] + 2 : match_pos[1] - 2]

            if tag_content.endswith(".png"):
                tag = f'<img src = "{os.path.join("..","Images",tag_content)}"></img>'
                line = line[:match_pos[0]-1] + tag + line[match_pos[1]:]
                # The -1 to the start index is to nab the ! from image tags
            else:
                tag = f'<a href = "{tag_content + ".html"}">{tag_content}</a>'
                line = line[:match_pos[0]]+ tag + line[match_pos[1]:]
            
            
        return line
    

    def createCssFile(self, template):
        css_file_path = os.path.join(self.dest_folder,"styles.css")
        with open(css_file_path,"w") as css_file:
            css_file.write(template)

    
    def createIndex(self, template):
        index_dir = os.path.join(self.dest_folder,"Note-Index.html")
        index_list_str = ""

        for file in self.md_files:
                file_name = os.path.basename(file).split(".")[0]
                index_list_str += (f'<li><a href = "{os.path.join("Notes",file_name)}.html" >{file_name}</a></li>'+'\n')

        with open(index_dir,"w") as index_file:
            index_file.write(template.format(index_list_str))
  
        
        