import os
import shutil

def organize_files(directory):
    # Define file types and corresponding folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".pdf", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Others": []  # Default folder for other file types
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))

    # Create an 'Others' folder if it doesn't exist
    others_folder = os.path.join(directory, "Others")
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)

    # Iterate through files and move them to respective folders
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1].lower()

            moved = False
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder)
                    new_filename = filename

                    # Check for duplicate files
                    while os.path.exists(os.path.join(destination_folder, new_filename)):
                        base_name, ext = os.path.splitext(new_filename)
                        base_name += "_copy"
                        new_filename = base_name + ext

                    shutil.move(
                        os.path.join(directory, filename),
                        os.path.join(destination_folder, new_filename)
                    )
                    print(f"Moved '{filename}' to {folder}")
                    moved = True
                    break
            else:
                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(others_folder, filename)
                )
                print(f"Moved '{filename}' to Others folder")