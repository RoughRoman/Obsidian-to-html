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
		
        self.geometry("450x150")
        self.title("Obsidian to HTML")

        self.vault_group = ttk.Frame(self)
        self.vault_group.pack(fill = tk.BOTH, expand = True)
        self.select_vault_button = ttk.Button(self.vault_group, text = "Select vault", width = 20,
		command = self.selectVault)
        self.select_vault_label = ttk.Label(self.vault_group, textvariable = self.vault_path )
        self.select_vault_button.pack(side = tk.LEFT)
        self.select_vault_label.pack(side = tk.LEFT, padx = 50)
        self.dest_group = ttk.Frame(self)
        self.dest_group.pack(fill = tk.BOTH, expand = True)
        self.select_dest_button = ttk.Button(self.dest_group,
                                            text = "Select destination",
                                            width = 20,
											command= self.selectDestFolder)
        self.select_dest_button.pack(side = tk.LEFT)
        self.dest_folder_label = ttk.Label(self.dest_group,
                                          textvariable= self.dest_folder_path)
        self.dest_folder_label.pack(side = tk.LEFT, padx = 50)
        self.convert_button = ttk.Button(self, text = "Convert!", width = 20,
		command = self.convert)
        self.convert_button.pack(padx = 20, pady = 20)

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

        
