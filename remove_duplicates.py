import os
import hashlib

def remove_duplicates(directory):
    # Create a dictionary to store file hashes
    file_hashes = {}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            if file_hash in file_hashes.values():
                print(f"Removing duplicate file: {filename}")
                os.remove(file_path)
            else:
                file_hashes[filename] = file_hash