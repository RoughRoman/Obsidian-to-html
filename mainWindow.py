import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
from tkinter import messagebox
import os
from converter import Converter

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.vault_path = tk.StringVar(self, "No Vault Selected")
        self.dest_folder_path = tk.StringVar(self, "No Destination set")

        self.title("Obsidian to HTML")

        self.select_vault_label = ttk.Label(self, textvariable = self.vault_path )
        self.select_vault_button = ttk.Button(self, text = "Select a vault: ", command = self.selectVault)
        self.select_vault_label.grid(row = 0, column = 1)
        self.select_vault_button.grid(row = 0, column = 0)
        self.convert_button = ttk.Button(self, text = "Convert!", command = self.convert)
        self.convert_button.grid(row = 1, column = 0)

        self.dest_folder_label = ttk.Label(self,
                                          textvariable= self.dest_folder_path)
        self.select_dest_button = ttk.Button(self,
                                            text = "Select a destination Folder",
                                            command= self.selectDestFolder)
        self.dest_folder_label.grid(row= 1, column=1)
        self.select_dest_button.grid(row= 1, column=0)


        self.mainloop()

    def selectVault(self):
        self.vault_path.set(filedialog.askdirectory(initialdir="."))

    def convert(self):
        converter = Converter(str(self.vault_path.get()),
                              str(self.dest_folder_path.get()))
        

        if os.path.isdir(str(self.vault_path.get())):
            answer = messagebox.askyesnocancel("Question", "Use Multiple Processors?"
                                               +" (Faster but will slow down your computer temporarily)")
            if answer:
                # convert with multi-threading
                converter.parseFile(parallel= True )
            elif answer == False:
                # convert with single thread
                converter.parseFile(parallel= False )
            else:
                # cancel
                return

        else:
            messagebox.showerror("Error", "Invalid path. Please select your vault directory folder.")

    def selectDestFolder(self):
        self.dest_folder_path.set(filedialog.askdirectory(initialdir="."))

        
