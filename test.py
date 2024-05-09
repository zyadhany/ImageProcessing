import cv2


import Process
from Process import EditWindow, Filter
import cv2

X = EditWindow(width=1300, height=720)

img = cv2.imread('tmp/lenna.png')
X.load_image(img)


X.switch_layer(1)
X.changePotion(x=700, y=200)
X.addFilter(Filter.Sobel)

X.editImage(img, 0, 0)

X.show()



