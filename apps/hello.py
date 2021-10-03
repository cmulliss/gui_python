import tkinter as tk
from tkinter import ttk

# main window is going to be called root
# Tk is creating an object, the main window
# .pack() puts the text into the window
root = tk.Tk()
ttk.Label(root, text="Hello World", padding=(30, 10)).pack()
# tells it to start running and continues until you close your window
root.mainloop()
