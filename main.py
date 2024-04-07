import tkinter as tk
from GUI import MainRoot, data

def add(x):
    x = 5
    return x

def main():
    root = tk.Tk()
    data.window_width = root.winfo_screenwidth()
    data.window_height = root.winfo_screenheight()
    MainRoot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
