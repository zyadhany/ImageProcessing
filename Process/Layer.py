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
            self._image = img
        else:
            self.width = width
            self.height = height
            self._image = np.ones((height, width, 3), np.uint8) * 255
        self.Filter = None
        self.x = 0
        self.y = 0

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
        return self.Filter.apply_filter(self._image)
    
    @image.setter
    def image(self, val):
        self._image = val
    
    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, val):
        self._Filter = val


