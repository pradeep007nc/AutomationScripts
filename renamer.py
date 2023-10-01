import os

def rename_images(directory_path, new_prefix):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Filter only image files (you can add more extensions if needed)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Rename each image file
    for index, old_name in enumerate(image_files, start=1):
        # Get the file extension
        _, extension = os.path.splitext(old_name)

        # Construct the new name with the specified prefix and index
        new_name = f"{new_prefix}_{index}{extension}"

        # Construct the full paths for old and new names
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {old_name} -> {new_name}')

# Example usage
directory_path = '/home/pilli007/Documents/MajorProject/MajorProjectFrontend/src/assets/mousepads'
new_prefix = 'mousepads'
rename_images(directory_path, new_prefix)
