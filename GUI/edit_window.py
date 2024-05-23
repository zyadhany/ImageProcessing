import tkinter as tk
from tkinter import Frame
from Process import EditWindow
import data
import os

def EditWindow_config():
    edt = EditWindow(tk_frame=data.EDIT_FRAME)
    edt.show()
    data.EDIT_WINDOW = edt