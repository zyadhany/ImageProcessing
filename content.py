import tkinter as tk
from tkinter import Frame
import os
import data

def MainContent(root):
    content = Frame(root, width=data.window_width,height=0.9*data.window_height,bg='red')
    #content = Frame(root, width=13,height=0.1*33,bg='red')
    content.pack_propagate(False)
    frame1=Frame(content ,width=0.03*data.window_width,height=data.window_height,bg='blue')
    frame1.place(x=0,y=0)

    #000000000000000000000000000000000000000000
    frame2=Frame(content , width=0.7*data.window_width,height=data.window_height,bg='white')
    frame2.place(x=0.09*data.window_width,y=0*data.window_height)
    #000000000000000000000000000000000000000000000000
    frame3=Frame( content, width=0.18*data.window_width,height=0.4*data.window_height,bg='yellow')

    frame3.place(x=0.84*data.window_width,y=0.4*data.window_height)
#000000000000000000000000000000000000000000000000000000000000000000000


    #frame4=Frame(width=0.18*data.window_width,height=0.08*data.window_height,bg='white')
    #frame4.place(x=0.8*data.window_width,y=0.6*data.window_height)


#00000000000000000000000000000000000000000000000000000000
#  put  photo inside frame2import tkinter as tk

    image = tk.PhotoImage(file="flowers 3.jpg")
    label = tk.Label(content, image=image)
    label.pack()



    return (content)       