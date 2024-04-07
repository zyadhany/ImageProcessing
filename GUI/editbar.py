import tkinter as tk
from tkinter import Frame
from . import data
import os

def MainEditBar(root):
    editbar = Frame(root, width=data.window_width,height=0.1*data.window_height,bg='grey')
    editbar.pack_propagate(False)
    return (editbar)
