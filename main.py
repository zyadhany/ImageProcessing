import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2
from GUI import MainRoot
import data
import threading
import subprocess

def req():
    data.EDIT_WINDOW.load_image_fromfile('tmp/lenna.png')
    data.EDIT_WINDOW.render()
    image = Image.fromarray(data.EDIT_WINDOW.image)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(data.EDIT_FRAME, image=photo)
    label.image = photo
    label.pack()
    cv2.imshow('w', data.EDIT_WINDOW.image)

    return
    #data.EDIT_WINDOW.tk_frame = None
    data.EDIT_WINDOW.show()
    data.EDIT_WINDOW.show()

def main():
    root = tk.Tk()
    data.ROOT = root
    data.window_width = root.winfo_screenwidth()
    data.window_height = root.winfo_screenheight()
    MainRoot(root)
    #req()
    root.mainloop()

    
if __name__ == "__main__":
    main()
