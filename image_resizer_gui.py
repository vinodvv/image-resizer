"""
Tkinter-based desktop application for batch image resizing.

This app lets users select one or more image files, choose a resize
percentage (30%, 50%, or 75%), and save resized copies into a separate
output folder using the Pillow library. Supported formats include
common image types such as JPEG, PNG, GIF, BMP, and WebP.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


class ImagerResizerApp:
    """
    Main application class for Image Resizing

    Tkinter GUI application for resizing selected images by a percentage.

        The app allows users to:
        - Select multiple image files from disk
        - Choose a resize scale (30%, 50%, or 75%)
        - Save resized copies to a configurable output folder

        Resizing is performed with Pillow while preserving aspect ratio by
        scaling both width and height by the same factor.
"""

    def __init__(self, root):
        """Initialize the app - this runs when you create the app"""
        # Store the root window so we can use it in other methods
        self.root = root

        # Set up window properties
        self.root.title("Image Resizer")
        self.root.geometry("500x500")
        self.root.configure(bg="#f5f5f5")

        # Declare variables
        self.output_folder = "resized_images"
        self.supported_formats = (
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'
        )
        self.scale_factor = 50  # Default scale is 50%
        self.selected_images = []

        # Build the user interface
        self.setup_ui()

    def setup_ui(self):
        """Build the main interface"""
        # Create main container frame
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Title
        title = tk.Label(
            main_frame,
            text="Image Resizer",
            font=("Arial", 16, "bold"),
            fg="#333333"
        )
        title.pack(pady=10)

        # File select button
        tk.Button(
            main_frame,
            text="Select image(s)",
            font=("Arial", 12),
            bg="#1976d2",
            fg="white",
            command=self.select_images,
            relief="flat",
            cursor="hand2",
        ).pack(pady=5, expand=True, fill="x", padx=(0, 5))

        # List box to display selected images
        self.list_images = tk.Listbox(
            main_frame,
            width=60,
            height=10,
            font=("Arial", 11),
            relief="solid",
        )
        self.list_images.pack(fill="x", expand=True, padx=(0, 5), pady=5)

        # Label showing count of selected images
        self.images_count_label = tk.Label(
            main_frame,
            text="0 images selected",
            font=("Arial", 12),
        )
        self.images_count_label.pack(pady=5)

        # Frame for resize options
        buttons_frame =tk.Frame(main_frame, bg="#f5f5f5")
        buttons_frame.pack(fill="x", expand=True, padx=10, pady=10)

        # Resize options
        tk.Button(
            buttons_frame,
            text="Reduce to 30%",
            bg="#1976d2",
            fg="white",
            font=("Arial", 10),
            relief="flat",
            cursor="hand2",
            command=self.set_resize_30
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        tk.Button(
            buttons_frame,
            text="Reduce to 50%",
            bg="#1976d2",
            fg="white",
            font=("Arial", 10),
            relief="flat",
            cursor="hand2",
            command=self.set_resize_50
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        tk.Button(
            buttons_frame,
            text="Reduce to 75%",
            bg="#1976d2",
            fg="white",
            font=("Arial", 10),
            relief="flat",
            cursor="hand2",
            command=self.set_resize_75
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Resize button
        tk.Button(
            main_frame,
            text="Resize",
            bg="#388e3c",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.resize_images
        ).pack(fill="x", expand=True, padx=20, pady=(0, 10))

        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Ready and resize set to 50%.",
            font=("Arial", 10),
            fg="#666666"
        )
        self.status_label.pack(pady=10)

    def select_images(self):
        """Open file dialog and store the selected image(s) file paths"""
        images = filedialog.askopenfilenames(
            title="Select image(s) files to resize",
            filetypes=[("Image Files", self.supported_formats)]
        )
        # Convert to list so it's easier to manipulate
        self.selected_images = list(images)
        self.update_image_list()

    def update_image_list(self):
        """Refresh the listbox and file count label with current selections"""
        # Clear the list box
        self.list_images.delete(0, tk.END)

        # Loop through images
        for i, image in enumerate(self.selected_images, start=1):
            # Show only the file name with an index prefix
            filename = f"{i} - {os.path.basename(image)}"
            self.list_images.insert(tk.END, filename)

        # Update image count label
        self.images_count_label.config(
            text=f"{len(self.selected_images)} images selected to resize."
        )

    def resize_images(self):
        """Resize and save the selected image files into the specified output folder"""
        # Check at least one image file selected
        if not self.selected_images:
            messagebox.showwarning(
                "No images selected",
                "Please select at least one image file to resize."
            )
            return

        # Create output directory if not exists
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        self.status_label.config(text="Resizing images...")

        # Loop through each image file and resize
        try:
            for image_path in self.selected_images:
                with Image.open(image_path) as img:
                    # Calculate new size
                    width, height = img.size
                    new_width = int(width * (self.scale_factor / 100.0))
                    new_height = int(height * (self.scale_factor / 100.0))

                    # Ensure dimensions are at least 1
                    new_width = max(1, new_width)
                    new_height = max(1, new_height)

                    resized_img = img.resize(
                        (new_width, new_height),
                        resample=Image.LANCZOS
                    )

                    # Save with new name
                    basename = os.path.basename(image_path)
                    output_path = os.path.join(self.output_folder, f"resized_{basename}")
                    resized_img.save(output_path)

            self.status_label.config(
                text=f"Images resized and saved to folder: {self.output_folder}."
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to resize images: {str(e)}"
            )

    def set_resize_30(self):
        """Set scale factor to 30% when button reduce to 30% clicked"""
        self.scale_factor = 30
        self.status_label.config(text="Resize set to 30%.")

    def set_resize_50(self):
        """Set scale factor to 50% when button reduce to 50% clicked"""
        self.scale_factor = 50
        self.status_label.config(text="Resize set to 50%.")

    def set_resize_75(self):
        """Set scale factor to 75% when button reduce to 75% clicked"""
        self.scale_factor = 75
        self.status_label.config(text="Resize set to 75%.")


# =================================================
# RUN THE APP
# =================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = ImagerResizerApp(root)
    root.mainloop()
