import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def refresh_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", f"Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination_folder)

    messagebox.showinfo("Success", f"All files from '{source_folder}' have been copied to '{destination_folder}'.")

def on_refresh_button_click():
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    destination_folder = filedialog.askdirectory(title="Select Destination Folder (Joy)")

    if source_folder and destination_folder:
        refresh_files(source_folder, destination_folder)

# Create the GUI
root = tk.Tk()
root.title("File Refresh Automation")

refresh_button = tk.Button(root, text="Refresh", command=on_refresh_button_click)
refresh_button.pack(pady=20)

root.mainloop()