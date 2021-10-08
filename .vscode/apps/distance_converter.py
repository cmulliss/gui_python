import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry("600x400")
# root.resizable(False, False)
root.title("Distance Converter")

# create a variable that will hold the value in our entry field, assign it by adding textvariable to metres_input
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")

# define a fn that will run when we click the button
# using try, except in case button clicked when no input, then link to button below, command=calculate_feet
# link feet_value to our display, as we did with enter field
def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:3f}")
    except ValueError:
        pass


# make column one expand to fill the space, so as window expands, by pulling corner, stays in centre
root.columnconfigure(0, weight=1)

# create a frame and add widgets
main = ttk.Frame(root, padding=(30, 15))
# puts it into the container, root, using the grid algorithm, defaults to row 0, and column 0, ie, top left
main.grid()

metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value)
feet_label = ttk.Label(main, text="Feet")
feet_display = ttk.Label(main, text="Feet shown here: ", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate ", command=calculate_feet)

# now place all our elements into the mainframe using grid
metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)


root.mainloop()


# sticky="W" to left align labels
# button to take up full space, sticky="EW"
# to stop crowding, add padding to all elements, padx=5, pady=5
