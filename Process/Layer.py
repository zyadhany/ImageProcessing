import cv2
import numpy as np

class Layer:
    """
    Represents a layer in the EditWindow.

    Attributes:
        width (int): The width of the layer in pixels.
        height (int): The height of the layer in pixels.
        x, y (int): coordinate of the first pixel of image.
        image (numpy.ndarray): The image data for the layer.
    """

    def __init__(self, width=0, height=0, img=None):
        """ Initialize a Layer object. """
        if img is not None:
            self.height, self.width, _ = img.shape
            self.image = img
        else:
            self.width = width
            self.height = height
            self.image = np.ones((height, width, 3), np.uint8) * 17
        self.x = 0
        self.y = 0

    def draw_circle(self, x, y, radius, color):
        """ Draws a filled circle on the layer. """
        cv2.circle(self.image, (x, y), radius, color, -1)
