import tkinter as tk
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def getPath(file_path):
    return os.path.join(current_directory, file_path)

def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def rootConfig(root:tk.Tk):
    
    # name and icon
    root.title("Simulation")
    #root.iconbitmap(getPath("resource/icon.ico"))

    # size
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.config(width=window_width, height=window_height)

    root.attributes('-fullscreen', False)
    root.bind("<F11>", lambda event:toggle_fullscreen(root))
    root.bind("<Escape>", lambda event:root.quit())

    return root