import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

# create a variable, tk not ttk widget as very simple
# user can type 8 lines of text
text = tk.Text(root, height=8)
text.pack()

# inserting text into the text area
# first line, and zero character
text.insert("1.0", "Please enter a comment... ")
# can disable a text area
text["state"] = "normal"  # or can be disabled

# retrieve content from a text area
# give starting and ending positions for text retrieval
text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()
