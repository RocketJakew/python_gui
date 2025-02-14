 # This is a GUI test in python

# Goal is to create a application gui that allows the user to search the local computer for a 
# xlsx file uploads the xlsx file and the xlsx file is then transformed in a json format which can then be sent using an api
import tkinter as tk
import pandas as pd 
from tkinter import filedialog
import json
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
 
def open_file_browser():
    global filename
    file_path = filedialog.askopenfilename()
    
    if file_path:
        filename = file_path

def generate_json_schema():
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "routineShortages": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "subject": {"type": "string"},
                                "shortageStatus": {"type": "string"},
                                "shortagePeriod": {
                                    "type": "object",
                                    "properties": {
                                        "start": {"type": "string", "format": "date"},
                                        "end": {"type": "string", "format": "date"}
                                    },
                                    "required": ["start", "end"]
                                },
                                "authorisationCountry": {"type": "string"},
                                # "shortageRootCauses": {
                                #     "type": "array",
                                #     "items": {"type": "string"}
                                # }
                            },
                            "required": ["subject", "shortageStatus", "authorisationCountry"]
                        }
                    }
                },
                "required": ["items"]
            }
        },
        "required": ["routineShortages"]
    }
    return json.dumps(schema, indent=4) 

def fill_json_from_dataframe(df):
    items = []
    for _, row in df.iterrows():
        item = {
            "subject": str(row["PMS ID (Packaged medicinal product)"]),
            "shortageStatus": row["Shortage status"],
            "authorisationCountry": row["Country of authorisation"]
        }
        
        if not pd.isna(row["Shortage start date"]) and not pd.isna(row["Shortage end date"]):
            item["shortagePeriod"] = {
                "start": row["Shortage start date"].strftime("%Y-%m-%d"),
                "end": row["Shortage end date"].strftime("%Y-%m-%d")
            }
        
        if not pd.isna(row["Root cause of shortage"]):
            try:
                item["shortageRootCauses"] = row["Root cause of shortage"].split(";")#str(int(float(row["Root cause of shortage"].split(";"))))  # Ensure it's an integer
            except ValueError:
                pass  # Skip if it can't be converted

        items.append(item)
    
    return {"routineShortages": {"items": items}}  # Now returns a dictionary


def save_json_to_file(json_data, output_file):
    with open(output_file, "w") as f:
        json.dump(json_data, f, indent=4)
        #f.write(json_data)

def convert_to_json():
    df = pd.read_excel(filename)
    json_data = fill_json_from_dataframe(df)
    save_json_to_file(json_data, "/home/admin_jan/projects/python_gui/output.json")

# 
# Create the main window
root = tk.Tk()
root.title("ESMP Converter & Upload")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Browse", command=open_file_browser)
button.pack()

start_process = tk.Button(root, text="Start Process", command=convert_to_json)
start_process.pack()

# Run the application
root.mainloop()
