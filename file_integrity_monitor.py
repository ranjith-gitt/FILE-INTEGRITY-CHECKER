import hashlib
import os
import time

# Define a function to calculate the hash value of a file
def calculate_hash(file_path):
    hash_value = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_value.update(chunk)
    return hash_value.hexdigest()

# Define a function to monitor changes in files
def monitor_files(file_paths):
    # Initialize a dictionary to store the initial hash values
    initial_hashes = {}
    for file_path in file_paths:
        initial_hashes[file_path] = calculate_hash(file_path)

    # Continuously monitor the files for changes
    while True:
        for file_path in file_paths:
            current_hash = calculate_hash(file_path)
            if current_hash != initial_hashes[file_path]:
                print(f"Change detected in file: {file_path}")
                print(f"Initial Hash: {initial_hashes[file_path]}")
                print(f"Current Hash: {current_hash}")
                initial_hashes[file_path] = current_hash  # Update the initial hash
        time.sleep(5)  # Wait for 5 seconds before checking again

# Define the file paths to monitor
file_paths = ['D:/Internship/GT SOFTWARE ACADEMY.docx']

# Run the file integrity monitor
monitor_files(file_paths)
