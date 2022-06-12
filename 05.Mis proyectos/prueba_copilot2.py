# Program to convert pdf file to jpg file
    # Import the necessary modules
import os 
import sys
import pdf2image

    # Function to convert pdf file to jpg file
def convert_pdf_to_jpg(file_name):
    # Check if the file exists
    if not os.path.isfile(file_name):
        print('File ' + file_name + ' does not exist')
        sys.exit(1)
    # Convert the pdf file to jpg file
    pdf = pdf2image.convert_from_path(file_name)
    # Get the name of the file
    file_name = file_name.split('.')[0]
    # Create a folder to store the jpg files
    if not os.path.exists(file_name):
        os.makedirs(file_name)
    # Loop through all the pages of the pdf file
    for page in pdf:
        # Save the page as a jpg file
        page.save(file_name + '/' + str(pdf.index(page)) + '.jpg', 'JPEG')
    # Print the name of the file
    print('File ' + file_name + ' converted')
    # Exit the program
    sys.exit(0)
    # End of program

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
    # Convert the pdf file to jpg file
    convert_pdf_to_jpg(file_name)
    # Exit the program
    sys.exit(0)
# End of program
