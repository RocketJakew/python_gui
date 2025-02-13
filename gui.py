# This is a GUI test in python

# Goal is to create a application gui that allows the user to search the local computer for a 
# xlsx file uploads the xlsx file and the xlsx file is then transformed in a json format which can then be sent using an api
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Run the application
root.mainloop()