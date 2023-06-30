import os

def upload_photo():
    # Create folder if it doesn't exist
    folder_name = "folder1"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Prompt user for photo file path
    photo_path = input("Enter the path of the photo file: ")

    # Check if the file exists
    if not os.path.isfile(photo_path):
        print("File not found.")
        return

    # Get the file name from the path
    photo_name = os.path.basename(photo_path)

    # Create the destination path
    destination_path = os.path.join(folder_name, photo_name)

    # Copy the file to the destination folder
    try:
        with open(photo_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
            destination_file.write(source_file.read())
        print("Photo uploaded successfully.")
    except IOError as e:
        print(f"An error occurred while uploading the photo: {e}")

# Run the upload_photo function
upload_photo()
