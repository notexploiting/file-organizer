import os
import shutil
import argparse

# Define the default file type to folder mapping
FILE_TYPES = {
    'mp3': 'Music',
    'flac': 'Music',
    'wav': 'Music',
    'pdf': 'Documents',
    'docx': 'Documents',
    'doc': 'Documents',
    'txt': 'TextFiles',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'heic': 'Images',
    'gif': 'Images',
    'webp': 'Images',
    'xlsx': 'Spreadsheets',
    'csv': 'Spreadsheets',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'mp4': 'Videos',
    'avi': 'Videos',
    'mkv': 'Videos'
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
            source_file = os.path.join(dir, filename)
            destination_file = os.path.join(destination, filename)

            # Attempt to move the file into the destination 
            try:
                shutil.move(source_file, destination)
                print(f"Moved: {source_file} to {destination_file}")
            except Exception as e:
                print(f"Error moving {source_file} to {destination_file}: {e}")
        else:
            print(f"The file extension '{file_extension}' was not specified in the `FILE_TYPES` dictionary.")

if __name__ == '__main__':
    parser= argparse.ArgumentParser(description="A Python application that keeps your directories tidy by organizing files into folders based on their types")
    parser.add_argument('source_directory', type=str, help='The directory to organize')
    args = parser.parse_args()

    organize_files(args.source_directory)
    