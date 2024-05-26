import cv2
import numpy as np

class Filter():

    def __init__(self):
        pass

    def apply_filter(self, img):
        return img

class grayscale(Filter):
    def apply_filter(self, img, alpha=1.0, beta=0):
        """
            alpha: Contrast control (1.0-3.0)
            beta: Brightness control (0-100)
        """
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        adjusted_img = cv2.convertScaleAbs(gray_img, alpha=alpha, beta=beta)
        colorized_img = cv2.cvtColor(adjusted_img, cv2.COLOR_GRAY2BGR)
        
        return colorized_img


class Gaussian_Blur(Filter):
    def apply_filter(self, img, sz=15, dg=0):
        blurred_img = cv2.GaussianBlur(img, (sz,sz), dg)
        return (blurred_img)

class Sobel(Filter):
    def apply_filter(self, img):
        if len(img.shape) == 3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = img 
        
        sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

        gradient_mag = np.sqrt(sobel_x**2 + sobel_y**2)

        gradient_mag_color = cv2.cvtColor(gradient_mag.astype(np.uint8), cv2.COLOR_GRAY2BGR)

        return gradient_mag_color

