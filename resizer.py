"""
THE APP:
Batch image resizer that processes all images in a folder and resizes
them to 50% of their original size using the Pillow library.
"""

# Import necessary libraries
import os
from PIL import Image

# Print header
print("Batch Image Resizer")
print("====================\n")

# Define folders
INPUT_DIR = 'images'
OUTPUT_DIR = 'resized_images'

# Define formats and new image scale
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
SCALE_FACTOR = 0.5

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get list of image files from input folder
print("Scanning images folder...")

if not os.path.isdir(INPUT_DIR):
    print(f"Input folder '{INPUT_DIR}' not found.")
    raise SystemExit(1)

image_files = [image for image in os.listdir(INPUT_DIR) if image.lower().endswith(SUPPORTED_FORMATS)]

if not image_files:
    print("No supported image files found. Nothing to do.")
    raise SystemExit(0)

print(f"Found {len(image_files)} images to resize\n")

# Print processing header
print("Processing images....")
print("----------------------")

success = 0
failed = 0

# Loop through each image file
for filename in image_files:
    # Build full path to input image and output image
    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Open the image
    try:
        with Image.open(input_path) as img:
            # Calculate new dimensions (50% of original)
            new_width = int(img.width * SCALE_FACTOR)
            new_height = int(img.height * SCALE_FACTOR)

            # Print resizing info
            print(f"Resizing: {filename} ({img.width}x{img.height}) -> ({new_width}x{new_height})")

            # Resize the image
            resized_img = img.resize(
                (new_width, new_height),
                resample=Image.Resampling.LANCZOS
            )

            # Save resized image
            resized_img.save(output_path)
            print(f"✔️ Saved to: {output_path}\n")
            success += 1
    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")
        failed += 1

# Print completion message
print(f"[SUCCESS]: Resized {success} image(s), failed: {failed}.")
