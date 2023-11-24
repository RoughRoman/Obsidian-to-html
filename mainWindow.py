import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

import os

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.vault_path = tk.StringVar(self, "No Vault Selected")

        self.title("Obsidian to HTML")

       
        self.select_vault_label = ttk.Label(self, textvariable = self.vault_path )
        self.select_vault_button = ttk.Button(self, text = "Select a vault: ", command=self.selectVault)
        self.select_vault_label.grid(row = 0, column = 1)
        self.select_vault_button.grid(row = 0, column = 0)




        self.mainloop()

    def selectVault(self):
        self.vault_path.set(filedialog.askdirectory())
        print(self.vault_path)