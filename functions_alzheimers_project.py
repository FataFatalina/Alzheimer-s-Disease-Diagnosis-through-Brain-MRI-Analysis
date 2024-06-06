#-----------------------------------------------------------------------------------------------
def get_file_names(directory):
    """
    Appends the names of the files contained in the given directory to a list.

    :param directory: Path to the directory from which to list file names
    :return: List of file names contained in the directory
    """
    # Initialize an empty list to store file names
    file_names = []
    
    # Use os.listdir to get all entries in the directory
    for entry in os.listdir(directory):
        # Join the directory path with the entry name to get the full path
        full_path = os.path.join(directory, entry)
        
        # Check if the entry is a file and not a directory
        if os.path.isfile(full_path):
            # Append the file name to the list
            file_names.append(entry)
    
    return file_names


#-----------------------------------------------------------------------------------------------

import os

def retrieve_image_paths(root_dir, extension='.nii'):
    """
    Retrieve full paths of files with a given extension from a root directory and all its subdirectories.
    
    :param root_dir: The directory to search for files.
    :param extension: The file extension to look for. Defaults to '.nii'.
    :return: A list of full paths to the files that have the specified extension.
    """
    image_paths = []
    # Walk through all directories and files within the root directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter files with the specified extension
        for filename in filenames:
            if filename.endswith(extension):
                # Create the full path to the file and add it to the list
                full_path = os.path.join(dirpath, filename)
                image_paths.append(full_path)
    return image_paths


#-----------------------------------------------------------------------------------------------

import nibabel as nib
import matplotlib.pyplot as plt

# Function to load and display multiple NIfTI images given a list of file paths
def display_images(nifti_file_paths):
    for file_path in nifti_file_paths:
        img = nib.load(file_path)
        data = img.get_fdata()
        # Choosing a slice to display. Here we choose the middle slice of the first dimension.
        slice_0 = data[data.shape[0] // 2, :, :]
        
        plt.imshow(slice_0.T, cmap='gray', origin='lower')
        plt.title(f"NIfTI Image Display: {file_path}")
        plt.axis('off')  # Turn off axis numbers and ticks
        plt.show()


