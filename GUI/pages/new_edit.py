from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter import simpledialog
from Process import EditWindow
from ..edit_window import EditWindow_config

WINDOW = None
ROOT = None

def close_modal(modal, root):
    root.attributes('-disabled', False)
    modal.destroy()

def create_model(model, root, width, height):
    print(width, height)
    edt = EditWindow(width=int(width), height=int(height))
    EditWindow_config(edt)
    close_modal(model, root)

def new_frame(parent: tk.Tk):
    # Create the modal window
    window = tk.Toplevel(parent)
    window.geometry("754x289")
    window.configure(bg="#D0C4C4")
    window.title("New Project")
    window.overrideredirect(True)

    WINDOW = window
    ROOT = parent

    canvas = Canvas(
        window,
        bg="#D0C4C4",
        height=289,
        width=754,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(file="resource/assest/button_1_new.png")
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_modal(WINDOW, ROOT),
        relief="flat"
    )
    button_1.place(
        x=450.0,
        y=231.0,
        width=249.0,
        height=31.0
    )

    button_image_2 = PhotoImage(file="resource/assest/button_2_new.png")
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_model(WINDOW, ROOT, entry_1.get(), entry_2.get()),
        relief="flat"
    )
    button_2.place(
        x=58.0,
        y=231.0,
        width=249.0,
        height=31.0
    )

    canvas.create_text(
        57.0,
        70.0,
        anchor="nw",
        text="Width\n",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_image_1 = PhotoImage(file="resource/assest/entry_1_new.png")
    canvas.create_image(
        223.0,
        79.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=129.0,
        y=69.0,
        width=188.0,
        height=18.0
    )

    canvas.create_text(
        448.0,
        72.0,
        anchor="nw",
        text="Height\n",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_image_2 = PhotoImage(file="resource/assest/entry_2_new.png")
    canvas.create_image(
        614.0,
        81.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=520.0,
        y=71.0,
        width=188.0,
        height=18.0
    )

    button_image_3 = PhotoImage(file="resource/assest/button_3_new.png")
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=201.0,
        y=157.0,
        width=355.0,
        height=20.0
    )

    canvas.create_text(
        129.0,
        158.0,
        anchor="nw",
        text="Color\n",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    window.grab_set()
    parent.eval(f'tk::PlaceWindow {window} center')
    parent.wait_window(window)
