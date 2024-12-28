import os
import shutil
from tkinter import Tk, filedialog, simpledialog, messagebox

def copy_project():
    """Copies the Flutter project to a selected destination."""
    # Prompt user to select the source folder
    messagebox.showinfo("Select Source Folder", "Please select your Flutter project folder.")
    source = filedialog.askdirectory(title="Select Project Folder")
    if not source:
        messagebox.showerror("No Folder Selected", "You didn't select a source folder. Operation cancelled.")
        return None, None

    # Prompt user to select the destination folder
    messagebox.showinfo("Select Destination Folder", "Please select the destination folder where you want to copy the project.")
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if not destination:
        messagebox.showerror("No Folder Selected", "You didn't select a destination folder. Operation cancelled.")
        return None, None

    # Set destination path
    project_name = os.path.basename(source)
    dest_path = os.path.join(destination, project_name)
    
    # Copy the entire directory
    try:
        shutil.copytree(source, dest_path)
        messagebox.showinfo("Success", f"Project copied successfully to:\n{dest_path}")
        return source, dest_path
    except FileExistsError:
        messagebox.showerror("Folder Already Exists", "A folder with the same name already exists in the destination.")
        return None, None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while copying the project:\n{e}")
        return None, None

def rename_project_folder(dest_path):
    """Prompts the user to rename the copied project folder."""
    if not dest_path:
        return
    
    # Get the parent directory and current folder name
    parent_dir = os.path.dirname(dest_path)
    current_name = os.path.basename(dest_path)
    
    # Prompt for a new name
    new_name = simpledialog.askstring(
        "Rename Folder",
        f"Enter a new name for the project folder (current name: {current_name}):"
    )
    if not new_name:
        messagebox.showinfo("No Rename", "Folder renaming skipped.")
        return

    # Set the new folder path
    new_dest_path = os.path.join(parent_dir, new_name)
    
    # Rename the folder
    try:
        os.rename(dest_path, new_dest_path)
        messagebox.showinfo("Success", f"Folder renamed successfully to:\n{new_dest_path}")
        return new_dest_path
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while renaming the folder:\n{e}")
        return dest_path

def replace_file_in_project(dest_path):
    """Replaces the specific file in the copied project."""
    if not dest_path:
        return
    
    # Target file path in the copied project
    target_file_path = os.path.join(dest_path, "ios", "Runner", "GoogleService-Info.plist")
    
    # Prompt user to select the replacement file
    messagebox.showinfo("Select Replacement File", "Please select the new GoogleService-Info.plist file to copy.")
    source_file = filedialog.askopenfilename(
        title="Select New File",
        filetypes=[("Property List Files", "*.plist"), ("All Files", "*.*")]
    )
    if not source_file:
        messagebox.showerror("No File Selected", "You didn't select a file for replacement. Operation cancelled.")
        return

    # Ensure the target directory exists
    target_dir = os.path.dirname(target_file_path)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)  # Create the directory if it doesn't exist

    # Copy and replace the file
    try:
        shutil.copy2(source_file, target_file_path)  # Copy with metadata preservation
        messagebox.showinfo("Success", f"File replaced successfully:\n{target_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while replacing the file:\n{e}")

def main():
    # Initialize tkinter GUI
    root = Tk()
    root.withdraw()  # Hide the root window
    
    # Step 1: Copy the Flutter project
    source, dest_path = copy_project()
    
    # Step 2: Rename the project folder
    if dest_path:
        dest_path = rename_project_folder(dest_path)
    
    # Step 3: Replace the specific file in the copied project
    if dest_path:
        replace_file_in_project(dest_path)

if __name__ == "__main__":
    main()
