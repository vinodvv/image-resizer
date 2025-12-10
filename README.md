# Image Resizer

A simple Python image resizer with both a command-line interface (CLI) and a desktop GUI built with Tkinter.  
The app uses the Pillow library to batch resize images to a smaller percentage of their original size.

## Features

- CLI tool:
  - Scans a folder for supported image formats
  - Resizes all images to 50% of their original dimensions
  - Saves output images in a `resized_images` folder

- GUI app:
  - Select specific image files from any folder
  - Choose resize percentage: 30%, 50%, or 75%
  - Displays a list of selected images
  - Saves resized images as `resized_<original_name>` in `resized_images`

Supported formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`.

## Requirements

- Python 3.8+
- Pillow
- Tkinter (bundled with most standard Python installations)

Install Pillow:

```bash
    pip install pillow
```

## Project structure

image-resizer/
├─ resizer.py
├─ resizer_gui.py
├─ images/ # Optional sample input folder for CLI
├─ resized_images/ # Output folder (created automatically)
├─ README.md
└─ LICENSE


Adjust filenames to match your actual scripts.

## Usage

### 1. CLI – batch resize a folder

Place your images in the `images` folder (or change `INPUT_DIR` in the script), then run:

```bash
    python resizer.py
```

The script will:

- Scan the input folder for supported image types  
- Resize each image to 50% of its original width and height  
- Save output files into the `resized_images` folder

### 2. GUI – select images and resize

Run the GUI script:

```bash
    python resizer_gui.py
```

Workflow:

1. Click **“Select image files”** and choose one or more images.
2. Choose a resize option: **Reduce to 30%**, **50%**, or **75%**.
3. Click **“Resize”** to process the selected files.
4. Resized images are saved to the `resized_images` folder with `resized_` prefixed to the filename.

## Notes and limitations

- The app resizes images by a percentage; it does not currently set exact width/height values.
- Aspect ratio is preserved by scaling both width and height by the same factor.
- Existing files with the same output name may be overwritten in the output folder.

## Future improvements

- Add options for custom percentage or target width/height.
- Option to choose the output folder from the GUI.
- Basic people/face detection to optionally skip photos containing people.
- Progress bar and better error reporting in the GUI.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
