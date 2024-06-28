import os
import shutil
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def refresh_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", f"Source folder '{source_folder}' does not exist.")
        return

    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)  # Remove the existing destination folder to avoid conflicts

    shutil.copytree(source_folder, destination_folder)  # Copy the entire directory tree

    messagebox.showinfo("Success", f"All files and folders from '{source_folder}' have been copied to '{destination_folder}'.")

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        file_data = file.read()
    
    if old_text not in file_data:
        messagebox.showinfo("Info", f"The text '{old_text}' was not found in the file '{file_path}'.")
        return

    file_data = file_data.replace(old_text, new_text)
    
    with open(file_path, 'w') as file:
        file.write(file_data)
    
    messagebox.showinfo("Success", f"The text '{old_text}' has been replaced with '{new_text}' in the file '{file_path}'.")

def search_and_replace_text(destination_folder):
    file_name = simpledialog.askstring("Input", "Enter the name of the file to search for:")
    if not file_name:
        return

    old_text = simpledialog.askstring("Input", "Enter the text to search for:")
    if not old_text:
        return

    new_text = simpledialog.askstring("Input", "Enter the new text to replace with:")
    if not new_text:
        return

    found = False
    for root, dirs, files in os.walk(destination_folder):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            replace_text_in_file(file_path, old_text, new_text)
            found = True
            break

    if not found:
        messagebox.showinfo("Info", f"The file '{file_name}' was not found in the destination folder.")

def on_refresh_button_click():
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    destination_folder = filedialog.askdirectory(title="Select Destination Folder (Joy)")

    if source_folder and destination_folder:
        refresh_files(source_folder, destination_folder)

def on_search_and_replace_button_click():
    destination_folder = filedialog.askdirectory(title="Select Destination Folder (Joy)")
    
    if destination_folder:
        search_and_replace_text(destination_folder)

# Create the GUI
root = tk.Tk()
root.title("File Automation")

refresh_button = tk.Button(root, text="Refresh", command=on_refresh_button_click)
refresh_button.pack(pady=10)

search_and_replace_button = tk.Button(root, text="Search and Replace", command=on_search_and_replace_button_click)
search_and_replace_button.pack(pady=10)

root.mainloop()