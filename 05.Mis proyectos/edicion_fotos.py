# Program that edits photos with openCV and tkinter
import cv2
import tkinter as tk

# Function that edits the photo
def edit_photo(photo, photo_name):
    # Load the photo
    img = cv2.imread(photo)
    # Create a window
    cv2.namedWindow(photo_name, cv2.WINDOW_NORMAL)
    # Show the photo
    cv2.imshow(photo_name, img)
    # Wait for a key press
    cv2.waitKey(0)
    # Close the window
    cv2.destroyAllWindows()

if __name__ == '__main__':

    # Create a window
    root = tk.Tk()
    # Create a label
    label = tk.Label(root, text='Select a photo')
    # Create a button
    button = tk.Button(root, text='Select', command=lambda: edit_photo(photo.get(), photo_name.get()))
    # Create a textbox
    photo = tk.Entry(root)

    # Create a textbox
    photo_name = tk.Entry(root)

    # Place the label and button
    label.pack()
    button.pack()
    photo.pack()
    photo_name.pack()

    # Start the main loop
    root.mainloop()
    # Close the window
    root.destroy()
    # Edit the photo
    edit_photo(photo.get(), photo_name.get())
    # Exit the program
    exit()

