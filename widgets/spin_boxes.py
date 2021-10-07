import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

initial_value = tk.IntVar(value=20)
spin_box = ttk.Spinbox(root, from_=0, to=30, textvariable=initial_value, wrap=False)

spin_box.pack()

print(spin_box.get())

root.mainloop()

# can use ttk version of spin_box
# instead of from and to, can use a set of values:
# values=(5, 10, 15, 20, 25, 30)
