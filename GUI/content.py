import tkinter as tk
from tkinter import Frame
import os
from . import data
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.9*data.window_height,bg='red')

    center_x = root.winfo_reqwidth() // 2
    center_y = root.winfo_reqheight() // 2
    content.pack_propagate(False)
    

    # Create the content frame
    fe = Frame(content, width=center_x, height=center_y + 100, bg='white')
    fe.place(relx=0.5, rely=0.45, anchor='center')
    
    tk_image = ImageTk.PhotoImage(file="tmp/lenna.png")

    fe.pack_propagate(False)
    # Create a Label widget with the image
    label = tk.Label(fe, image=tk_image)
    label.image = tk_image  # Keep a reference to the image to prevent garbage collection
    # Pack the label inside the frame
    label.pack()


    return (content)