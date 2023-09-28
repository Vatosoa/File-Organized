import os

from remove_duplicates import remove_duplicates
from organize_file import organize_files

if __name__ == "__main__":
    print("Welcome to Your File Organizer!")
    directory = input("Enter the directory to organize: ")

    if os.path.exists(directory):
        # Step 1: Organize files
        organize_files(directory)
        print("Files organized successfully.")

        # Step 2: Remove duplicate files
        print("\nRemoving duplicate files...")
        remove_duplicates(directory)
        print("Duplicate files removed.")

        # Step 3: Display summary report
        print("\nSummary Report:")
        total_files = sum(len(files) for _, _, files in os.walk(directory))
        print(f"Total Files: {total_files}")

        for root, dirs, files in os.walk(directory):
            for folder in dirs:
                print(f"Folder '{folder}': {len(os.listdir(os.path.join(root, folder)))} files")

    else:
        print("Error: Directory does not exist.")