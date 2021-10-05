import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()

root.title("Greeter")

# tell tkinter to grow rows and columns as much as possible. By default columns have a weight of 0, which means they only taku the amount of space of their content. Elements now being centred in window.
root.columnconfigure(0, weight=1)

# creates a placeholder for a string coming from an entry field
user_name = tk.StringVar()

# input frame goes in 1st row
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

# entry field, both go into input_frame, instead of root
name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10), sticky="EW")
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

# buttons frame goes in 2nd row
buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)
# or can use a tuple:
# "buttons.columnconfigure((0,1),weight=1)

# put buttons into buttons frame
# greeting button
greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")

# quit button
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()

# needs 2 frames


# pack can make layouts complicated, so can use grid instead
# grid allows us to define a 2 deep table where our widgets will be placed within a container
