import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# if want to use later, assign to variable and put pack on second line
label = ttk.Label(root, text="Hello World!", padding=20)
label.pack()

# separator
ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="Hello World!", padding=20).pack()


root.mainloop()
