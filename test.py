import tkinter as tk
from PIL import Image, ImageTk

class ImageBackgroundCanvas(tk.Canvas):
    def __init__(self, parent, image_path, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Load the image
        self.image = Image.open(image_path)
        self.photo_image = ImageTk.PhotoImage(self.image)

        # Create the canvas image item
        self.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # Set the size of the canvas to the size of the image
        self.config(width=self.image.width, height=self.image.height)

if __name__ == "__main__":
    root = tk.Tk()

    # Path to the image file
    image_path = 'resource\edt_bgimage.png'

    # Create the canvas with the image background
    canvas = ImageBackgroundCanvas(root, image_path)
    canvas.pack()

    root.mainloop()
