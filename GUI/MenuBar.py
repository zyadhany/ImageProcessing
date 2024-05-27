from tkinter import Frame, Menu, filedialog
import tkinter as tk
from Process import file_load, save_as
from .edit_window import EditWindow_config, render_edit
from .pages import new_frame
import data
from .content import edit_frame

def get_file_path():
    try:
        file = filedialog.askopenfilename(title="chose folder")
    except FileNotFoundError:
        return None
    return file

def load_edit_file():
    path = get_file_path()
    edt = file_load(path)
    edit_frame(edt.width, edt.height)
    EditWindow_config(edt)

def open_image_from_file():
    path = get_file_path()
    if path == '':
        return
    try:
        data.EDIT_WINDOW.load_image_fromfile(path)
        render_edit()
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
    
def menu_save():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("imaged", "*.png *.jpg *.jpeg"), ("All files", "*.*")]
    )
    data.EDIT_WINDOW.save_image(file_path)    

def menu_save_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("editfile", "*.zh"), ("All files", "*.*")]
    )
    tk_tmp = data.EDIT_WINDOW.tk_frame

    data.EDIT_WINDOW.tk_frame = None


    for ly in data.EDIT_WINDOW.layers:
        ly.tk_images = None

    save_as(data.EDIT_WINDOW, file_path)
    
    data.EDIT_WINDOW.tk_frame = tk_tmp
    render_edit()


def MakeMenu(root):
    bar=Menu(root)
    root.config(menu=bar)
    # File in menubar
    filemenu=Menu(bar,tearoff=0)
    bar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=lambda: new_frame(data.ROOT))
    filemenu.add_command(label='Load ', command=load_edit_file)
    filemenu.add_command(label='Open ', command=open_image_from_file)
    filemenu.add_command(label='Save ', command=menu_save)
    filemenu.add_command(label='Save AS ', command=menu_save_as)
    filemenu.add_separator()
    filemenu.add_command(label='Print')
    filemenu.add_command(label='Close')
    #000000000000000000000000000000000
    # Eidt in menubar
    editmenu=Menu(bar,tearoff=0)
    bar.add_cascade(label='Edit', menu=editmenu)
    editmenu.add_command(label='Undo')
    editmenu.add_command(label='Redo')
    editmenu.add_separator()
    editmenu.add_command(label='Cut')
    editmenu.add_command(label='Copy')
    editmenu.add_command(label='Paste')
    editmenu.add_command(label='Delete')

    #0000000000000000000000000000000000000000000000
    #imgae in menubar
    imagemenu=Menu(bar,tearoff=0)
    bar.add_cascade(label='Image', menu=imagemenu)
    imagemenu.add_command(label='Resize')
    imagemenu.add_command(label='Rotate')
    imagemenu.add_command(label='Flip')
    imagemenu.add_command(label='Brightness and Contrast')
    imagemenu.add_separator()
    imagemenu.add_command(label='Colors')
    imagemenu.add_command(label='Effects')
    #0000000000000000000000000000000000000000000000000000000

    # tool in menubar
    toolmenu=Menu(bar,tearoff=0)
    bar.add_cascade(label='TOOls', menu=toolmenu)
    toolmenu.add_command(label='Brush')
    toolmenu.add_command(label='Pencil')
    toolmenu.add_command(label='Line')
    toolmenu.add_command(label='Shape')
    toolmenu.add_command(label='Text')

    #00000000000000000000000000000000000000000000000
    # view in menubar
    viewmenu=Menu(bar,tearoff=0)
    bar.add_cascade(label='View', menu=viewmenu)
    viewmenu.add_command(label='Zoom In')
    viewmenu.add_command(label='Zoom Out')
    viewmenu.add_command(label='Zoom to Fit')
    pass