import tkinter as tk
from tkinter import Frame
import os
import data
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL
from . imageviewer import EditViewApp

def edit_frame(width=720, height=720):
    width = 720
    height = 720
    if width is 0:
        width = data.ROOT.winfo_reqwidth() // 2
    if height is 0:
        height = data.ROOT.winfo_reqheight() // 2
   
    if data.EDIT_FRAME:
        data.EDIT_FRAME.destroy()
    
    edit = Frame(data.CONTENT_WINDOW, bg='white')
    edit.config(width=width, height=height)
    edit.place(relx=0.5, rely=0.45, anchor='center')
    edit.pack_propagate(False)
    view = EditViewApp(edit)
    view.pack(expand=True, fill=tk.BOTH)

    data.EDIT_FRAME = edit
    data.EDIT_VIEW_APP = view

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.9*data.window_height, bg='#5D3E8C')
    content.pack_propagate(False)
    data.CONTENT_WINDOW = content

    
    # Create the edit frame
    edit_frame()
    

    # Add layer and navgation
    #
    #

    return (content)