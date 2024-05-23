import tkinter as tk
from tkinter import Frame
import os
import data
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.9*data.window_height, bg='#5D3E8C')
    content.pack_propagate(False)

    
    # Create the edit frame
    center_x = root.winfo_reqwidth() // 2
    center_y = root.winfo_reqheight() // 2
    edit = Frame(content, bg='white')
    edit.config(width=center_x, height=center_y)
    edit.place(relx=0.5, rely=0.45, anchor='center')
    edit.pack_propagate(False)
    data.EDIT_FRAME = edit
    

    # Add layer and navgation
    #
    #

    return (content)