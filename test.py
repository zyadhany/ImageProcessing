import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np

class YourClass:
    def __init__(self):
        self.image = np.random.randint(244, 245, size=(300, 300, 3), dtype=np.uint8)
        self.image_1 = None  # Keep a reference to the PhotoImage objects
        self.image_2 = None

    def create_frame(self, parent, index):
        lyf = tk.Frame(parent, width=350, height=73)
        lyf.pack_propagate(False)
        lyf.pack()

        self._canvas = Canvas(
            lyf,
            bg="#FFB8B8",
            height=73,
            width=326,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self._canvas.pack(side="left", fill="both", expand=True)

        pil_image_1 = Image.fromarray(self.image[..., ::-1]).resize((50, 50))
        self.image_1 = ImageTk.PhotoImage(pil_image_1)

        image_1 = self._canvas.create_image(
            36.669189453125,
            36.0,
            image=self.image_1
        )


# Example usage
root = tk.Tk()
your_object = YourClass()
your_object.create_frame(root, 0)
root.mainloop()
