import tkinter as tk
from tkinter import Frame
import data
import os

def EditConfig(root):
    editbar = Frame(root, width=data.window_width,height=0.1*data.window_height,bg='#171435')
    editbar.pack_propagate(False)
    return (editbar)