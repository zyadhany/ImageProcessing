import cv2
import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk
import numpy as np
from .Layer import Layer
import copy

class EditWindow():
    """
    Represents an editing window with multiple layers.

    Attributes:
        width (int): The width of the editing window in pixels.
        height (int): The height of the editing window in pixels.
        layers (list): A list of Layer objects representing the layers in the editing window.
        defult_layer (img): defult layer to create.
        current_layer (int): The index of the currently active layer.
        image (img): final image after compine all layers.
    """

    count_name = 1

    def __init__(self, width=720, height=520, tk_frame:Tk=None, fileload=None, default_layer=None):
        """ Initializes an EditWindow object. """
        if fileload:
            self.file_load(fileload)
            return
        
        self.tk_frame:Tk = tk_frame
        if tk_frame is not None:
            self.width = tk_frame.winfo_reqwidth()
            self.height = tk_frame.winfo_reqheight()
        else:
            self.width = width
            self.height = height
    
        self.current_layer = 0
        if default_layer:
            self.default_layer = default_layer
        else:
            self.default_layer = Layer(self.width, self.height)
        self.layers = []
        self.add_layer()
        self.switch_layer(0)
        self.render()

    def editImage(self, img, x=0, y=0):
        self.getCurLayer().addImage(img, x, y)

    def addFilter(self, filt):
        self.getCurLayer().Filter = filt

    def changePotion(self, x=None, y=None):
        if x is not None:
            self.getCurLayer().x = x
        if y is not None:
            self.getCurLayer().y = y

    def getCurLayer(self):
        return self.layers[self.current_layer]

    def swap_layers(self, lef, rig):
        if lef < 0 or lef >= len(self.layers):
            return
        if rig < 0 or rig >= len(self.layers):
            return
        if lef == rig:
            return
        self.layers[lef], self.layers[rig] = self.layers[rig], self.layers[lef]
        if lef == self.current_layer:
            self.switch_layer(rig)
        elif rig == self.current_layer:
            self.switch_layer(lef)
    
    def switch_layer(self, layer_index):
        """ Switches the currently active layer. """
        self.layers[self.current_layer].current = 0
        if 0 <= layer_index < len(self.layers):
            self.current_layer = layer_index
        self.layers[self.current_layer].current = 1

    def add_layer(self, ly=None):
        """ add layer to window"""
        if ly is None:
            ly = copy.deepcopy(self.default_layer)
            ly.name = f"Layer {self.count_name}"
            self.count_name += 1
        self.layers.append(ly)
        self.render()
        pass

    def remove_layer(self, index):
        """ remove layer to window"""
        if len(self.layers) == 1 or index >= len(self.layers):
            # print error massage
            return

        if index <= self.current_layer:
            self.switch_layer(self.current_layer - 1)
        elif index == self.current_layer and index == len(self.layers) - 1:
            self.switch_layer(self.current_layer - 1)
        del self.layers[index]
        self.switch_layer(self.current_layer)
        self.render()

    def render(self):
        """ Combine all layers into one image. """
        result = copy.deepcopy(self.default_layer.image)

        for layer in self.layers:
            # Determine the bounding box to copy the layer onto the result image
            start_x = min(layer.x, self.width)
            start_y = min(layer.y, self.height)
            end_x = min(layer.x + layer.width, self.width)
            end_y = min(layer.y + layer.height, self.height)

            # Copy the layer onto the result image at the appropriate position
            result[start_y:end_y, start_x:end_x] = layer.image[:end_y - start_y, :end_x - start_x]

        self.image = result

    def save_image(self, filename):
        """ Saves into image """
        self.render()
        cv2.imwrite(filename, self.image)

    def load_image_fromfile(self, image_path):
        """ Loads an image from a file. """
        image = cv2.imread(image_path)
        self.load_image(img=image)

    def load_image(self, img):
        """ Loads an image from a file. """
        layer = Layer(img=img)
        self.layers.append(layer)

    def show(self):
        """ view the final image. """
        self.render()
        if self.tk_frame is None:
            cv2.imshow('Edit Window', self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            image = Image.fromarray(self.image[..., ::-1])
            #image.show()
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.tk_frame, image=photo)
            label.image = photo
            label.place(x=-2, y=-2)
    
    def __str__(self):
        return f"width:{self.width}, height:{self.height}, num_layers:{len(self.layers)}"
    
    def __repr__(self):
        return f"width:{self.width}, height:{self.height}, num_layers:{len(self.layers)}"

