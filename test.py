import tkinter as tk
from PIL import Image, ImageTk

class ImageEditor:
    def __init__(self, master):
        self.master = master
        master.title("Image Editor")

        # Create navigation bar frame
        self.nav_bar_frame = tk.Frame(master, bg="lightblue", height=50)
        self.nav_bar_frame.pack(fill=tk.X, expand=True)

        # Create content frame
        self.content_frame = tk.Frame(master)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Placeholder image label
        self.image_label = tk.Label(self.content_frame)
        self.image_label.pack()

        # Button to open image file
        self.open_button = tk.Button(self.nav_bar_frame, text="Open Image", command=self.open_image)
        self.open_button.pack(side=tk.LEFT, padx=10)

        # Add more editing buttons here (brightness, contrast, etc.)
        # ...

        # Function to open an image file
    def open_image(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.gif")])
        if filename:
            self.image = Image.open(filename).resize((400, 300))  # Resize for display
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo  # Keep reference

# Create the main window
root = tk.Tk()
image_editor = ImageEditor(root)

root.mainloop()
