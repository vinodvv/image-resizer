"""
THE APP:
Image resizer that processes all selected images and resizes
them to 30%, 50%, or 75% of their original size using the Pillow library.
"""

import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Define output folder
OUTPUT_DIR = "resized_images"

# Define formats supported and new image scale
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
SCALE_FACTOR = 50  # Default scale 50%

selected_images = []

def select_images():
    """Open file dialog and store the selected image(s) file paths"""
    global selected_images
    images = filedialog.askopenfilenames(
        title = "Select image(s) files to resize",
        filetypes = [("Image Files", SUPPORTED_FORMATS)]
    )
    # Convert to list so it's easier to manipulate
    selected_images = list(images)
    update_image_list()

def update_image_list():
    """Refresh the listbox and file count label with current selections."""
    list_images.delete(0, tk.END)

    for i, image in enumerate(selected_images, start=1):
        # Show only the file name with an index prefix
        file_name = f"{i} - {os.path.basename(image)}"
        list_images.insert(tk.END, file_name)

    # Update image count label
    images_count_label.config(
        text=f"{len(selected_images)} images selected to resize."
    )


def resize_images():
    """
    Resize and save the  selected image(s) files into
    the specified output folder
    """
    global SCALE_FACTOR

    # Check at least one image file selected
    if not selected_images:
        messagebox.showwarning(
            "No images selected",
            "Please select at least one image file to resize.")
        return

    # Create output directory if not exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    status_label.config(text="Resizing images...")
    root.update_idletasks()

    # Loop through each image file and resize
    try:
        for image_path in selected_images:
            with Image.open(image_path) as img:
                # Calculate new size
                width, height = img.size
                new_width = int(width * (SCALE_FACTOR // 100))
                new_height = int(height * (SCALE_FACTOR // 100))

                # Ensure dimensions are at least 1
                new_width = max(1, new_width)
                new_height = max(1, new_height)

                resized_img = img.resize(
                    (new_width, new_height),
                    resample=Image.LANCZOS
                )

                # Save with new name
                base_name = os.path.basename(image_path)
                output_path = os.path.join(OUTPUT_DIR, f"resized_{base_name}")
                resized_img.save(output_path)

        status_label.config(text=f"Images resized and saved to folder: {OUTPUT_DIR}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize images: {str(e)}")


def set_resize_30():
    """Set scale factor to 30% when button 30% is clicked"""
    global SCALE_FACTOR
    SCALE_FACTOR = 30
    status_label.config(text="Resize set to 30%.")

def set_resize_50():
    """Set scale factor to 50% when button 50% is clicked"""
    global SCALE_FACTOR
    SCALE_FACTOR = 50
    status_label.config(text="Resize set to 50%.")

def set_resize_75():
    """Set scale factor to 75% when button 75% is clicked"""
    global SCALE_FACTOR
    SCALE_FACTOR = 75
    status_label.config(text="Resize set to 75%.")



# ------- GUI setup -----
# Main window
root = tk.Tk()
root.title("Image Resizer")
root.geometry("480x480")

# Label title
label_title = tk.Label(root, text="Image Resizer", font=("Helvetica", 16))
label_title.pack(pady=20)

# Select files button widget
btn_choose_dir = tk.Button(
    text="Select image files", bg="blue", fg="white",
    font=("Helvetica", 12),
    command=select_images
)
btn_choose_dir.pack(pady=10)

# List box to display selected images
list_images = tk.Listbox(root, bg="lightgray", width=60, height=8, font=("Helvetica", 10))
list_images.pack(pady=10)

# Label showing count of selected images
images_count_label = tk.Label(root, text="0 images selected.", font=("Helvetica", 12))
images_count_label.pack()

# Frame to hold the resize buttons
frame_resize = tk.Frame(root)
frame_resize.pack(padx=10, pady=10)

# Create buttons for different sizes for resizing
btn_1 = tk.Button(
    frame_resize,
    text="Reduce to 30%", bg="green", fg="white",
    font=("Helvetica", 12),
    command=set_resize_30
)
btn_1.pack(side=tk.LEFT, padx=10, pady=5)

btn_2 = tk.Button(
    frame_resize,
    text="Reduce to 50%", bg="green", fg="white",
    font=("Helvetica", 12),
    command=set_resize_50
)
btn_2.pack(side=tk.LEFT, padx=10, pady=5)

btn_3 = tk.Button(
    frame_resize,
    text="Reduce to 75%", bg="green", fg="white",
    font=("Helvetica", 12),
    command=set_resize_75
)
btn_3.pack(side=tk.LEFT, padx=10, pady=5)

# Resize button to trigger the resizing
btn_resize = tk.Button(
    root,
    text="Resize", bg="blue", fg="white",
    font=("Helvetica", 15),
    command=resize_images
)
btn_resize.pack(pady=15)

# Show status
status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack()


if __name__ == "__main__":
    root.mainloop()
