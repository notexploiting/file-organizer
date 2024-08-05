import os
import shutil
import argparse

# Define the default file type to folder mapping
FILE_TYPES = {
    'exe': 'Executables',
    'mp3': 'Music'
}

def organize_files(dir):
    # Handle error where the path doesn't exist
    if not os.path.exists(dir):
        print('Specified path does not exist.')
        return
    
    # Iterate through the complete list of all files and directories in `dir`
    for filename in os.listdir(dir):
        # Ignore directories since we only want to deal with files; continue to the next iteration
        if os.path.isdir(os.path.join(dir, filename)):
            continue

        # Extract the file extension
        file_extension = filename.split('.')[-1]

        # Proceed with the organization only if `file_extension` is in our predefined list of extensions
        if file_extension in FILE_TYPES:
            destination = os.path.join(dir, FILE_TYPES[file_extension])

            # If our destination folder doesn't exist, create a new one
            if not os.path.exists(destination):
                os.makedirs(destination)
                print(f"Created folder: {destination}")

            # Move the file to the destination folder
            file = os.path.join(dir, filename)

            # To be added: try except for attempting to move file to folder

        else:
            print(f"The file extension '{file_extension}' was not specified in the `FILE_TYPES` dictionary.")

if __name__ == '__main__':
    # To be added: CLI 
    ...