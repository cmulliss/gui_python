import tkinter as tk
from tkinter import image_names, ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

# can add text from a variable
greeting = tk.StringVar()

image = Image.open(
    "/Users/cherry/repos/gui_python/apps/images/cherryPngPRofile.jpg"
).resize((64, 64))
photo = ImageTk.PhotoImage(image)
ttk.Label(root, image=photo, padding=5).pack()


label = ttk.Label(root, textvariable=greeting, padding=10, compound="right")
label.config(font=("Segoe UI", 20))
label.pack()

# set greeting text
greeting.set("Hello Cherry")

root.mainloop()
