import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

# 2 labels
rectangle_1 = tk.Label(root, text="Rectangle1", bg="green", fg="White")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle2", bg="red", fg="White")
rectangle_2.pack(ipadx=10, ipady=10, fill="both", expand=True)

root.mainloop()

# ipad internal spacing

# NB, Label reserves entire width for each label
# if use fill="x" will occupy entire space, that it already had

# side values
"""
default is side="top"
when side is top or bottom widgets take up all horiz space
when side left or right take up all the vertical space

widgets are pushed in the direction on their anchor point as far as possible within the available space
"""
