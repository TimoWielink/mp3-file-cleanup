# Rename all MP3 files to remove first carachters
#Timo Wielink 30 December 2022
import os

# Get the directory where the Python script is located
directory = os.path.dirname(os.path.abspath(__file__))

# Prompt the user to enter the target string to remove from the beginning of the filenames
print('Rename beginning of the file (e.g. [YT-MP3]')
target_string_beginning = input('Enter the target string to remove from the beginning of the filenames: ')

# Set the number of characters to remove from the beginning of the filenames to the length of the target string
num_chars_beginning = len(target_string_beginning)

# Prompt the user to enter the target string to remove from the end of the filenames
print('Rename end of the file (e.g. (320kbps)')
target_string_end = input('Enter the target string to remove from the end of the filenames: )')

# Remove the trailing white space character from the target string
target_string_end = target_string_end.rstrip()

# Set the number of characters to remove from the end of the filenames to the length of the target string
num_chars_end = len(target_string_end)

# Iterate through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an MP3 file
    if filename.endswith('.mp3'):
        # Check if the first `num_chars_beginning` characters of the filename match the target string
        if filename[:num_chars_beginning] == target_string_beginning:
            # Check if the last `num_chars_end` characters of the filename (before the '.mp3' extension) match the target string
            if filename[-num_chars_end-4:-4] == target_string_end:
                # Construct the full path of the file
                file_path = os.path.join(directory, filename)
                # Remove the first `num_chars_beginning` characters and the last `num_chars_end` characters from the filename
                new_filename = filename[num_chars_beginning:-num_chars_end-4] + '.mp3'
                # Construct the full path of the new filename
                new_file_path = os.path.join(directory, new_filename)
                # Print a message indicating that the file is being renamed
                print(f'Renaming file {filename} to {new_filename}...')
                # Rename the file
                os.rename(file_path, new_file_path)

# Print a message indicating that the script has finished running
print('Finished renaming files!')
