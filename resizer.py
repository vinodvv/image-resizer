# Import necessary libraries
import os
from PIL import Image

# Print header
print("Batch Image Resizer")
print("====================\n")

# Define folders
INPUT_DIR = 'images'
OUTPUT_DIR = 'resized_images'

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get list of image files from input folder
print("Scanning images folder...")

image_files = []

for image in os.listdir(INPUT_DIR):
    if image.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_files.append(image)

print(f"found {len(image_files)} images to resize\n")

# Print processing header
print("Processing images....")
print("----------------------")


# Loop through each image file
for filename in image_files:
    # Build full path to input image
    input_path = os.path.join(INPUT_DIR, filename)

    # Open the image
    img = Image.open(input_path)

    # Calculate new dimensions (50% of original)
    new_width = img.width // 2
    new_height = img.height // 2

    # Print resizing info
    print(f"Resizing: {filename} ({img.width}x{img.height}) -> ({new_width}x{new_height})")

    # Resize the image
    resized_img = img.resize((new_width, new_height))

    # Build output path and save
    output_path = os.path.join(OUTPUT_DIR, filename)
    resized_img.save(output_path)
    print(f"Saved to: {output_path}\n")

# Print completion message
print("All images resized successfully!")
