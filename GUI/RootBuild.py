from tkinter import Frame, Menu
import tkinter as tk
from .config import rootConfig, frameConfig
from .MenuBar import MakeMenu
from .edit_window import EditWindow_config

def MainRoot(root:tk.Tk):
    # configure proprites of the root
    rootConfig(root)

    # add frame to root.
    frameConfig(root)

    # Menu Bar confiig
    MakeMenu(root)
    
    # edit window congit
    EditWindow_config()

    return (root)
