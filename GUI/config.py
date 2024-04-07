import tkinter as tk
from tkinter import Frame
from .content import MainContent
from .editbar import MainEditBar
from . import data
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def getPath(file_path):
    return os.path.join(current_directory, file_path)

def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def rootConfig(root:tk.Tk):
    
    # name and icon
    root.title("Photoshop")
    #root.iconbitmap(getPath("resource/icon.ico"))

    # size
    root.config(width=data.window_width, height=data.window_height)
    print(data.window_height)
    root.maxsize(data.window_width, data.window_height)
    root.minsize(685,384)

    root.attributes('-fullscreen', False)
    root.bind("<F11>", lambda event:toggle_fullscreen(root))
    root.bind("<Escape>", lambda event:root.quit())

def frameConfig(root):
    editbar = MainEditBar(root)
    content = MainContent(root)
    editbar.pack()
    content.pack()