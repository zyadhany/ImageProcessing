from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\ImageProcessing\tmp\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1000x730")
window.configure(bg="black")

frame = Frame(window, bg="#FFB8B8")
frame.pack()

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

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(x=274.0, y=16.0, width=40.0, height=40.0)

canvas.create_rectangle(
    0.0,
    0.0,
    262.0,
    73.0,
    fill="#DDDDDD",
    outline=""
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    36.669189453125,
    36.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    230.0,
    36.0,
    image=image_image_2
)

canvas.create_text(
    79.948486328125,
    26.0,
    anchor="nw",
    text="asdasd",
    fill="#000000",
    font=("Inter", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
