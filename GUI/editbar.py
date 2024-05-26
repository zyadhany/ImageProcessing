import tkinter as tk
from tkinter import Frame
import data
import os

def MainEditBar(root):
    editbar = Frame(root, width=data.window_width,height=0.1*data.window_height,bg=data.EDIT_BG_COLOR)
    editbar.config(bd=1, relief='raised')
    editbar.pack_propagate(False)
    return (editbar)