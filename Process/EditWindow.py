import cv2
import numpy as np
from .Layer import Layer



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

    def __init__(self, width, height, fileload=None, defult_layer=None):
        """ Initializes an EditWindow object. """
        if fileload:
            self.file_load(fileload)
            return
        self.width = width
        self.height = height
        self.current_layer = 0
        if defult_layer:
            self.defult_layer = defult_layer
        else:
            self.defult_layer = Layer(width, height)
        self.layers = [self.defult_layer]
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

    def switch_layer(self, layer_index):
        """ Switches the currently active layer. """
        if 0 <= layer_index < len(self.layers):
            self.current_layer = layer_index
    
    def add_layer(self):
        """ add layer to window"""
        self.layers.append(self.defult_layer)
        self.render()
        pass

    def remove_layer(self, index):
        """ remove layer to window"""
        if len(self.layers) == 1:
            # print error massage
            return
        if index < self.current_layer:
            self.current_layer -= 1
        elif index == self.current_layer and index == len(self.layers):
            self.current_layer -= 1
        del self.layers[self.current_layer]
        self.render()

    def render(self):
        """ Combine all layers into one image. """
        result = self.defult_layer.image

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

    def load_image(self, img):
        """ Loads an image from a file. """
        layer = Layer(img=img)
        self.layers.append(layer)

    def show(self):
        """ view the final image. """
        self.render()
        cv2.imshow('Edit Window', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def __str__(self):
        return f"width:{self.width}, height:{self.height}, num_layers:{len(self.layers)}"
    
    def __repr__(self):
        return f"width:{self.width}, height:{self.height}, num_layers:{len(self.layers)}"

