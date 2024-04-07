from tkinter import Frame, Menu
import tkinter as tk
from .config import rootConfig, frameConfig
from .MenuBar import MakeMenu

def MainRoot(root:tk.Tk):
    # configure proprites of the root
    rootConfig(root)

    # add frame to root.
    frameConfig(root)

    # Menu Bar confiig
    MakeMenu(root)
    
    return (root)
