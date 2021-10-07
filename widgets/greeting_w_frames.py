import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()

# creates a placeholder for a string coming from an entry field
user_name = tk.StringVar()

# input frame
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

# entry field, both go into input_frame, instead of root
name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

# buttons frame
buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

# put buttons into buttons frame
# greeting button
greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left")

# quit button
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()

# needs 2 frames
