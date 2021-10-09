import tkinter as tk
from tkinter import ttk


# define an init method to call the super class of tk.Tk just so it performs an initialisation, using super etc.
# super().__init__() is the same as saying self = tk.Tk(), decause it calls the constructor of tk.Tk, so gives an app window and all the initialisation that happens within an object, happens in self. So, can now do self.title etc.
class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        ttk.Label(self, text="Hello World").pack()


# When we assign this root variable to the HelloWold object, root and self are the same thing.
root = HelloWorld()
root.mainloop()


# creating our own class for the app window, instead of using tk.Tk we are going to create our own class to hold root.

# we are now able to split our app into multiple classes.
