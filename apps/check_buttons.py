import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

check_button = ttk.Checkbutton(root, text="Check me!")
check_button.pack()


root.mainloop()
