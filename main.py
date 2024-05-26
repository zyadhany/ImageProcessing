import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk
import numpy as np
import cv2
from GUI import MainRoot
import data
import threading
import subprocess

def after_render():
    from GUI.edit_window import render_edit
    data.EDIT_VIEW_APP.make_fit()
    render_edit()


def main():
    root = tk.Tk()
    data.ROOT = root
    data.window_width = root.winfo_screenwidth()
    data.window_height = root.winfo_screenheight()
    MainRoot(root)
    root.after(10, after_render)
    root.mainloop()

    
if __name__ == "__main__":
    main()
