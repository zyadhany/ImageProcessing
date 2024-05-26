import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    try:
        file = filedialog.askopenfilename(title="اختر صورة", filetypes=[("*.png *.jpg *.jpeg *.gif")])
        print(file)
    except FileNotFoundError:
        pass

window = tk.Tk()
window.title("برنامج فتح الصورة")
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="فتح", command=open_image)
menubar.add_cascade(label="ملف", menu=filemenu)
window.config(menu=menubar)

window.mainloop()
