# Function to unzip a file


import zipfile
import os
import sys
import shutil

# Function to copy a file
def copy_file(file_name):
    # Copy the file
    shutil.copy(file_name, 'copied_file.txt')
    # Print the name of the file
    print('File ' + file_name + ' copied')

# Function to unzip a file
def unzip_file(file_name):
    # Open the zip file
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        # Extract all the contents of the zip file
        zip_ref.extractall()
        # Close the zip file
        zip_ref.close()
        # Print the name of the file
        print('File ' + file_name + ' extracted')

# Function tu zip a file
def zip_file(file_name):
    # Open the zip file
    with zipfile.ZipFile(file_name, 'w') as zip_ref:
        # Add the file to the zip file
        zip_ref.write(file_name)
        # Close the zip file
        zip_ref.close()
        # Print the name of the file
        print('File ' + file_name + ' zipped')

# Main program
if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print('Usage: python prueba_copilot.py <file_name>')
        sys.exit(1)
    # Get the name of the file
    file_name = sys.argv[1]
    # Check if the file exists
    if not os.path.isfile(file_name):
        print('File ' + file_name + ' does not exist')
        sys.exit(1)
    # Copy the file
    copy_file(file_name)
    # Unzip the file
    unzip_file(file_name)
    # Zip the file
    zip_file(file_name)
    # Exit the program
    sys.exit(0)
# End of program
