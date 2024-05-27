import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np

mat = np.eye(3)

mat_inv = np.linalg.inv(mat)

affine_inv = (
    mat_inv[0, 0], mat_inv[0, 1], mat_inv[0, 2],
    mat_inv[1, 0], mat_inv[1, 1], mat_inv[1, 2]
)

print(affine_inv)
