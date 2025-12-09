"""
THE APP:
Batch image resizer that processes all images in a folder and resizes
them to 50% of their original size using the Pillow library.

WHAT TO FIGURE OUT:
- How do you list files in a directory?
- How do you filter files by extension?
- How do you create folders if they don't exist?
- How do you resize images with Pillow?
- How do you loop through multiple files?

START HERE:
First, just try to list all files in the images folder.
Then work on opening ONE image and resizing it.
Finally, add the loop to process all images.

KEY CONCEPT:
Use os.listdir() to get files in a folder.
Use os.makedirs() with exist_ok=True to create folders safely.
Use Image.open() to load images and .resize() to change dimensions.
Calculate new size by dividing width and height by 2 (or use // 2).
Use os.path.join() to build file paths correctly.
"""

# ---------------------------------------------
# THE CODE SKELETON

# Import necessary libraries
# (PIL for images, os for file operations)


# Print header


# Define folders
# (input folder and output folder paths)


# Create output folder if it doesn't exist
# (use os.makedirs with exist_ok=True)


# Get list of image files from input folder
# (use os.listdir and filter for image extensions)


# Print processing header


# Loop through each image file

# Build full path to input image


# Open the image


# Calculate new dimensions (50% of original)


# Print resizing info


# Resize the image


# Build output path and save


# Print completion message

