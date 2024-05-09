import tkinter as tk
from tkinter import *
from GUI import MainRoot, data


def main():
    root = tk.Tk()
    data.window_width = root.winfo_screenwidth()
    data.window_height = root.winfo_screenheight()
    MainRoot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
