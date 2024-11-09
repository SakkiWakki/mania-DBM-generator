import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

class MyApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mania DBM Generator")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, 
                         text="Please input a folder containing .osu files or drag a folder into this window. 10k+ maps will be ignored.",
                         wraplength=300)
        label.pack(pady=20)
        
        folder_frame = tk.Frame(self)
        folder_frame.pack(pady=10)

        # Folder path display
        self.folder_path_var = tk.StringVar()
        self.folder_display = tk.Entry(folder_frame, textvariable=self.folder_path_var, width=40)
        self.folder_display.pack(side=tk.LEFT, padx=5)

        # Folder selector button
        select_button = tk.Button(folder_frame, text="Select Folder", command=self.select_folder)
        select_button.pack(side=tk.LEFT, padx=5)
        
        # Drag-and-drop
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)

        select_button = tk.Button(folder_frame, text="Generate DBMs!", command=self.generate)
        select_button.pack(side=tk.LEFT, padx=5)

    def generate(self):
        pass

    def select_folder(self):
        """Open a dialog to select a folder and update the entry field."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_var.set(folder_path)

    def on_drop(self, event):
        """Handle folder drop and update the entry field with the folder path."""
        folder_path = event.data.strip() 
        if self.tk.call("file", "isdir", folder_path):
            self.folder_path_var.set(folder_path)
        else:
            self.folder_path_var.set("Invalid folder")
