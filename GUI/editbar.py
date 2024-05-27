import tkinter as tk
from tkinter import Frame, Button, Entry, Canvas
from .scrollable import ScrollableFrame_Herzotal
from Process import FILTERS
from PIL import ImageTk
import data
import os
from .edit_window import render_edit

def add_filter(filt):
    data.EDIT_WINDOW.getCurLayer().Filter = filt
    render_edit()

def create_filter_frame(self, par):
    fr = tk.Frame(par.scrollable_frame, width=100, height=100, bg='blue')
    fr.pack(side="left", padx=10, pady=10)
    self.tk_edt_img = ImageTk.PhotoImage(self.pil_img.resize((100, 100)))
    background_label = tk.Label(fr, image=self.tk_edt_img)
    background_label.place(relwidth=1, relheight=1)
    background_label.bind("<Button-1>", lambda event: add_filter(self.name))   


filtr_edt = []
for fr in FILTERS.values():
    fr.create_frame = create_filter_frame
    

def scrollfilter(par):
    if data.LAYER_SCROLLER is not None:
        data.LAYER_SCROLLER.destroy()

    ff = ScrollableFrame_Herzotal(par)
    ff.pack()

    for fr in FILTERS.values():
        tt = fr()
        tt.create_frame(ff)
        filtr_edt.append(tt)

def change_circle_color(canvas, color):
    try:
        canvas.itemconfig('circle', fill=color)
    except:
        return
    print(color)
    data.PEN_COLOR = color

def MainEditBar(root):
    editbar = Frame(root, width=data.window_width,height=0.15*data.window_height,bg=data.EDIT_BG_COLOR)
    editbar.config(bd=1, relief='raised')
    editbar.pack_propagate(False)
    filter_container = Frame(editbar, width=1300, height=editbar.winfo_reqheight() - 30)
    filter_container.pack(side="right", padx=20, pady=15)
    filter_container.pack_propagate(False)
    scrollfilter(filter_container)
    
    top_left_frame = Frame(editbar, bg=data.EDIT_BG_COLOR)
    top_left_frame.pack(side='left', anchor='n', padx=10, pady=10)

    draw_button = tk.Button(top_left_frame, text="Draw", command=lambda: setattr(data, 'MODE', 'Draw'), padx=10, pady=5)
    draw_button.pack(side='left', padx=5)

    delete_button = tk.Button(top_left_frame, text="Delete", command=lambda: setattr(data, 'MODE', 'Delete'), padx=10, pady=5)
    delete_button.pack(side='left', padx=5)

    move_button = tk.Button(top_left_frame, text="Move", command=lambda: setattr(data, 'MODE', 'Move'), padx=10, pady=5)
    move_button.pack(side='left', padx=5)

    hand_button = tk.Button(top_left_frame, text="Hand", command=lambda: setattr(data, 'MODE', 'Hand'), padx=10, pady=5)
    hand_button.pack(side='left', padx=5)

    bottom_left_frame = Frame(editbar, bg=data.EDIT_BG_COLOR)
    bottom_left_frame.pack(side='left', anchor='s', padx=10, pady=10)

    text_entry = Entry(bottom_left_frame, width=20)
    text_entry.pack(side='left', padx=5)

    circle_canvas = Canvas(bottom_left_frame, width=30, height=30, bg=data.EDIT_BG_COLOR, highlightthickness=0)
    circle = circle_canvas.create_oval(5, 5, 25, 25, fill="Black", tags='circle')
    circle_canvas.pack(side='left', padx=5)

    text_entry.bind("<Return>", lambda event: change_circle_color(circle_canvas, text_entry.get()))


    return (editbar)