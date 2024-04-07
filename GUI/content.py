import tkinter as tk
from tkinter import Frame
import os
from . import data

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.9*data.window_height,bg='red')
    #content = Frame(root, width=13,height=0.1*33,bg='red')
    content.pack_propagate(False)
    return (content)