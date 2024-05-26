import tkinter as tk           
from tkinter import filedialog 
from PIL import Image, ImageTk 
import math                    
import numpy as np             
import os                      

class EditViewApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pil_image = None
        self.create_widget()
        self.reset_transform()
        self.redraw_image()

    def set_image(self, filename):
        if not filename:
            return
        self.pil_image = Image.open(filename)
        self.zoom_fit(self.pil_image.width, self.pil_image.height)
        self.draw_image(self.pil_image)

    def create_widget(self):
        # Canvas
        self.canvas = tk.Canvas(self, background="black")
        #pil_image = Image.open('resource\edt_bgimage.png')
        #self.bg_image = ImageTk.PhotoImage(pil_image)
        #canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.canvas.pack(expand=True, fill=tk.BOTH)


        self.canvas.bind("<Button-1>", self.mouse_down_left)                   # MouseDown
        self.canvas.bind("<B1-Motion>", self.mouse_move_left)                  # MouseDrag
        self.canvas.bind("<Double-Button-1>", self.mouse_double_click_left)    # MouseDoubleClick
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)                     # MouseWheel

    def mouse_down_left(self, event):
        self.__old_event = event

    def mouse_move_left(self, event):
        if self.pil_image is None:
            return
        self.translate(event.x - self.__old_event.x, event.y - self.__old_event.y)
        self.redraw_image()
        self.__old_event = event

    def mouse_double_click_left(self, event):
        if self.pil_image is None:
            return
        self.zoom_fit(self.pil_image.width, self.pil_image.height)
        self.redraw_image()

    def mouse_wheel(self, event):
        if self.pil_image is None:
            return
        if event.delta > 0:
            self.scale_at(1.25, event.x, event.y)
        else:
            self.scale_at(0.8, event.x, event.y)
        self.redraw_image()
        
    def reset_transform(self):
        self.mat_affine = np.eye(3)

    def translate(self, offset_x, offset_y):
        mat = np.eye(3)
        mat[0, 2] = float(offset_x)
        mat[1, 2] = float(offset_y)
        self.mat_affine = np.dot(mat, self.mat_affine)

    def scale(self, scale: float):
        mat = np.eye(3)
        mat[0, 0] = scale
        mat[1, 1] = scale
        self.mat_affine = np.dot(mat, self.mat_affine)

    def scale_at(self, scale: float, cx: float, cy: float):
        self.translate(-cx, -cy)
        self.scale(scale)
        self.translate(cx, cy)

    def zoom_fit(self, image_width, image_height):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if image_width * image_height <= 0 or canvas_width * canvas_height <= 0:
            return
        self.reset_transform()
        scale = 1.0
        offsetx = 0.0
        offsety = 0.0

        if canvas_width * image_height > image_width * canvas_height:
            scale = canvas_height / image_height
            offsetx = (canvas_width - image_width * scale) / 2
        else:
            scale = canvas_width / image_width
            offsety = (canvas_height - image_height * scale) / 2
        self.scale(scale)
        self.translate(offsetx, offsety)

    def make_fit(self):
        self.zoom_fit(self.pil_image.width, self.pil_image.height)
        self.redraw_image()

    def draw_image(self, pil_image):
        if pil_image is None:
            return

        self.pil_image = pil_image

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        mat_inv = np.linalg.inv(self.mat_affine)

        affine_inv = (
            mat_inv[0, 0], mat_inv[0, 1], mat_inv[0, 2],
            mat_inv[1, 0], mat_inv[1, 1], mat_inv[1, 2]
        )

        dst = self.pil_image.transform(
            (canvas_width, canvas_height),
            Image.AFFINE,
            affine_inv,
            Image.NEAREST
        )
        im = ImageTk.PhotoImage(image=dst)
#        pil_image.show()
        self.canvas.create_image(
            0, 0,
            anchor='nw',
            image=im
        )

        self.image = im

    def redraw_image(self):
        if self.pil_image is None:
            return
        self.draw_image(self.pil_image)
    
    def convert_img(self, img):
        self.pil_image = Image.fromarray(img[..., ::-1])
        #self.pil_image = ImageTk.PhotoImage(image)
