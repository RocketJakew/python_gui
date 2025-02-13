 # This is a GUI test in python

# Goal is to create a application gui that allows the user to search the local computer for a 
# xlsx file uploads the xlsx file and the xlsx file is then transformed in a json format which can then be sent using an api
import tkinter as tk
import pandas as pd 


def on_button_click():
    label.config(text="Button Clicked!")
# Function to browse filesystem
def browseFiles():
 global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a Excel-pthFile",
                                          filetypes = ("Excel files",
                                                        "*.xlsx*")
                                                       )
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
 
def convert_to_json():
 print("Convert to JSON Function")
  df = pd.read_excel(filename)
 df.show()

# Create the main window
root = tk.Tk()
root.title("ESMP Converter & Upload")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Browse", command=browseFiles)
button.pack()

start_process = tk.Button(root, text="Start Process", command=convert_to_json)
start_process.pack()

# Run the application
root.mainloop()
