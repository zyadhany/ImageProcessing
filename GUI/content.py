import tkinter as tk
from tkinter import Frame
import os
import data
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL
from . imageviewer import EditViewApp
from .scrollable import ScrollableFrame
from Process import Layer
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def delete_Layer(index):
    from .edit_window import render_edit
    data.EDIT_WINDOW.remove_layer(index=index)
    render_edit()

def convert_layer(index):
    from .edit_window import render_edit
    data.EDIT_WINDOW.switch_layer(layer_index=index)
    render_edit()

def create_frame(self, parent, index):
        frame = tk.Frame(parent, width=350, height=73, bd=0.5, relief="solid")
        frame.pack_propagate(False)
        frame.pack(pady=10, padx=10)

        canvas = Canvas(
            frame,
            bg="#FFB8B8",
            height=73,
            width=326,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(side="left", fill="both", expand=True)
        canvas.bind("<Button-1>", lambda event, index=index: convert_layer(index=index))   

        self.tk_images = []

        self.tk_images.append(PhotoImage(file='resource/assest/button_1_lyr.png'))
        button_1 = Button(
            frame,
            image=self.tk_images[0],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: delete_Layer(index=index),
            relief="flat"
        )
        button_1.place(x=274.0, y=16.0, width=40.0, height=40.0)

        bg_color = '#E6E6E6'
        if self.current:
            bg_color = '#808080'

        canvas.create_rectangle(
            0.0,
            0.0,
            262.0,
            73.0,
            fill=bg_color,
            outline=""
        )

        pil_image_1 = Image.fromarray(self.image[..., ::-1]).resize((50, 50))
        self.tk_images.append(ImageTk.PhotoImage(pil_image_1))
        image_1 = canvas.create_image(
            36.669189453125,
            36.0,
            image=self.tk_images[1]
        )

        pil_image_1 = Image.fromarray(self.image[..., ::-1]).resize((20, 20))
        self.tk_images.append(ImageTk.PhotoImage(pil_image_1))
        image_2 = canvas.create_image(
            230.0,
            36.0,
            image=self.tk_images[2]
        )

        canvas.create_text(
            79.948486328125,
            26.0,
            anchor="nw",
            text=self.name,
            fill="#000000",
            font=("Inter", 20 * -1)
        )

def new_layer():
    from .edit_window import render_edit
    data.EDIT_WINDOW.add_layer()
    render_edit()

def move_layer(val=0):
    from .edit_window import render_edit
    cur = data.EDIT_WINDOW.current_layer
    nxt = cur + val
    data.EDIT_WINDOW.swap_layers(cur, nxt)
    render_edit()

Layer.create_frame = create_frame

def scrollEdit():
    if data.LAYER_SCROLLER is not None:
        data.LAYER_SCROLLER.destroy()

    ls = ScrollableFrame(data.SCROLL_LAYER_FRAME)
    ls.pack()


    for index in range(len(data.EDIT_WINDOW.layers) - 1, -1, -1):
        ly = data.EDIT_WINDOW.layers[index]
        ly.create_frame(ls.scrollable_frame, index)
    data.LAYER_SCROLLER = ls

def layer_bar():
    width = 400
    height = 500
   
    if data.LAYER_FRAME:
        data.LAYER_FRAME.destroy()
    lf = Frame(data.CONTENT_WINDOW, width=width, height=height, bg=data.EDIT_BG_COLOR)
    lf.config(bd=3, relief='raised')
    lf.pack(side='bottom', anchor='e')
    lf.pack_propagate(False)
    data.LAYER_FRAME = lf
    
    slf = tk.Frame(lf, width=380, height=400, bd=1, relief='ridge')
    slf.pack()
    slf.pack_propagate(False)
    data.SCROLL_LAYER_FRAME = slf

    # Create the buttons inside slf frame
    # Create the buttons inside slf frame
    new_button = tk.Button(lf, text="New", width=10, height=2, command=new_layer)
    up_button = tk.Button(lf, text="Up", width=10, height=2, command=lambda: move_layer(val=1))
    down_button = tk.Button(lf, text="Down", width=10, height=2, command=lambda: move_layer(val=-1))

    # Pack the buttons in the slf frame
    new_button.pack(side='left', padx=10, pady=10)
    up_button.pack(side='left', padx=10, pady=10)
    down_button.pack(side='left', padx=10, pady=10)
    
def edit_frame(width=720, height=720):
    width = 1366
    height = 720
    if width is 0:
        width = data.ROOT.winfo_reqwidth() // 2
    if height is 0:
        height = data.ROOT.winfo_reqheight() // 2
   
    if data.EDIT_FRAME:
        data.EDIT_FRAME.destroy()
    
    edit = Frame(data.CONTENT_WINDOW, bg='white')
    edit.config(bd=1, relief='raised')
    edit.config(width=width, height=height)
    edit.place(relx=0.3934, rely=0.5, anchor='center')
    edit.pack_propagate(False)
    view = EditViewApp(edit)
    view.pack(expand=True, fill=tk.BOTH)

    data.EDIT_FRAME = edit
    data.EDIT_VIEW_APP = view

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.85*data.window_height, bg=data.CONTENT_BG_COLOR)
    content.pack_propagate(False)
    data.CONTENT_WINDOW = content

    edit_frame()
    layer_bar()
    return (content)
