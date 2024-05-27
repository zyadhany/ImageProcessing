import cv2
import numpy as np
import tkinter as tk
from .Filter import FILTERS
from PIL import Image, ImageTk 
import data
import re

class Layer:
    """
    Represents a layer in the EditWindow.

    Attributes:
        width (int): The width of the layer in pixels.
        height (int): The height of the layer in pixels.
        x, y (int): coordinate of the first pixel of image.
        image (numpy.ndarray): The image data for the layer.
    """

    current = 0
    name = "None"

    def __init__(self, width=0, height=0, img=None):
        """ Initialize a Layer object. """
        if img is not None:
            self.height, self.width, _ = img.shape
            self._image = img
        else:
            self.width = width
            self.height = height
            self._image = np.ones((height, width, 3), np.uint8) * 255
        self.Filter = None
        self.x = 0
        self.y = 0

    def get_bgr_color(self, color):
        if re.match(r'^#[0-9A-Fa-f]{6}$', color):
            hex_color = color.lstrip('#')
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            return (b, g, r) 
        else:
            color_map = {
                'red': (0, 0, 255),
                'green': (0, 255, 0),
                'blue': (255, 0, 0),
                'white': (255, 255, 255),
                'black': (0, 0, 0),
                'yellow': (0, 255, 255),
                'purple': (128, 0, 128),
            }

            return color_map.get(color.lower(), (0, 0, 0))

    def draw_circ(self, x, y, color, size):
        color_bgr = self.get_bgr_color(color)

        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")

        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer.")

        cv2.circle(self._image, (x, y), size, color_bgr, -1)  # -1 fills the circle


    def addImage(self, img, x, y):
        if self.image is None:
            self.image = img
        else:
            x_start = min(self.x, x)
            y_start = min(self.y, y)
            x_end = max(self.x + self.image.shape[1], x + img.shape[1])
            y_end = max(self.y + self.image.shape[0], y + img.shape[0])

            self.x = x_start
            self.y = y_start

    @property
    def image(self):
        if self.Filter is None:
            return self._image
        return FILTERS[self.Filter].apply_filter(None, img=self._image)
    
    @image.setter
    def image(self, val):
        self._image = val
    
    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, val):
        self._Filter = val


