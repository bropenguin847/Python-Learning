"""
File Viewer Application with GUI

This Python application provides a graphical user interface (GUI) that allows users to:
- Open and read CSV or Excel (`.xlsx`) files.
- Display the file content in a tabular format using a `Treeview` widget.
- Scroll through the content with thick vertical and horizontal scrollbars for ease of navigation.

Features:
---------
1. **File Selection**:
   - Users can select a file through a dialog box.
   - Supported formats: CSV and Excel (`.xlsx`).

2. **Dynamic Table Display**:
   - The application dynamically generates columns based on the data in the file.
   - Each column is populated with the corresponding data from the file.

3. **Scrollbars**:
   - Thick horizontal and vertical scrollbars make navigation simple, especially for large datasets.

4. **Error Handling**:
   - The application handles exceptions gracefully and displays error messages if a file cannot be read.

How It Works:
-------------
1. The main window provides a button to open a file.
2. On selecting a valid CSV or Excel file, the application reads its content using the `pandas` library.
3. The data is displayed in a `Treeview` widget, with scrollbars for navigation.

Customization:
--------------
- The scrollbars' thickness can be adjusted in the `style.configure` section.
- Column widths in the `Treeview` can be set dynamically or statically, based on user preference.

Libraries Used:
---------------
- `pandas`: For reading and processing CSV and Excel files.
- `tkinter`: For creating the graphical user interface.
- `ttk`: For advanced GUI widgets like `Treeview` and styled scrollbars.

Dependencies:
-------------
- Install the required libraries using:
  pip install pandas openpyxl

Packaging as an Executable:
---------------------------
- Use `pyinstaller` to package the script into a `.exe` file:
  pyinstaller --onefile --noconsole file_viewer.py

This creates a standalone executable that can be shared with users.

Author: Keith Lim
Date:   January 2025
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

def open_file():
    """Will ask user to choose file type to open"""
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
    )
    if file_path:
        try:
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path)

            # Display the data in the treeview
            update_treeview(df)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to read file: {e}")

def update_treeview(df):
    # Clear existing data
    for row in tree.get_children():
        tree.delete(row)

    # Update columns
    tree["column"] = list(df.columns)
    tree["show"] = "headings"
    for col in df.columns:
        tree.heading(col, text=col)

    # Add data to treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    for col in df.columns:
        tree.column(col, width=150)

# Create main window
root = tk.Tk()
root.title("File Viewer")
root.geometry("800x600")

# Create Open File button
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Create a frame to hold the Treeview and scrollbars
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=30, pady=30)

# Create Treeview widget to display data
tree = ttk.Treeview(frame)

# Create horizontal scrollbar
x_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
x_scrollbar.pack(side="bottom", fill="x")

# Create vertical scrollbar
y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
y_scrollbar.pack(side="right", fill="y")

# Configure the Treeview to use the scrollbars
tree.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
tree.pack(expand=True, fill="both", side="left")

# Increase scrollbar thickness
style = ttk.Style()
style.configure("Horizontal.TScrollbar", thickness=30)  # Horizontal scrollbar
style.configure("Vertical.TScrollbar", thickness=100)    # Vertical scrollbar

# Add a status bar
status_bar = tk.Label(root, textvariable=status_var, relief="sunken", anchor="w")
status_bar.pack(side="bottom", fill="x", padx=10, pady=5)

root.mainloop()
