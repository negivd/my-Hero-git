#!/usr/bin/env python3
"""
backup.py
----------
This script performs file backups from a source directory to a destination directory.

Now it interacts with the user to ask for source and destination paths.

Features:
    - Asks user to enter source and destination folders
    - Copies all files from source to destination
    - Appends a timestamp if a file with the same name already exists in destination
    - Handles errors gracefully (e.g., missing directories)
"""

import os           # For file and directory operations
import shutil       # For copying files
from datetime import datetime  # For generating timestamps


# Step 1: Define a helper function to copy files safely
def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        # Check if destination directory exists, create if not
        if not os.path.exists(dest_dir):
            print(f"Destination directory '{dest_dir}' does not exist. Creating it now...")
            os.makedirs(dest_dir)

        # Loop through all files in the source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)

            # Skip subdirectories (backup files only)
            if os.path.isdir(source_path):
                continue

            dest_path = os.path.join(dest_dir, filename)

            # Step 2: Check if file already exists in destination
            if os.path.exists(dest_path):
                # Add timestamp to make filename unique
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_filename)
                print(f"File '{filename}' already exists. Saving as '{new_filename}'")

            # Step 3: Copy the file
            shutil.copy2(source_path, dest_path)
            print(f"Backed up: {filename} → {dest_path}")

        print("\nBackup completed successfully.")

    except Exception as e:
        # Catch and display any unexpected errors
        print(f"An error occurred during backup: {e}")


# Step 4: Main script execution
if __name__ == "__main__":
    print("=== File Backup Utility ===")

    # Ask user for source and destination directories
    source_directory = input("Enter the full path of the source directory: ").strip()
    destination_directory = input("Enter the full path of the destination directory: ").strip()

    # Call the backup function
    backup_files(source_directory, destination_directory)
