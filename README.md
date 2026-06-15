# Image Splitter (Grid-Based) 🖼️✂️

An automated Python utility for splitting large images containing multiple objects arranged in a grid into individual, uniform-sized cropped images. This tool is specifically designed to streamline dataset preparation for machine learning models such as **YOLO**, **TensorFlow**, and other object detection or classification frameworks.

## 🌟 Key Features

- **Custom Grid Configuration**: Easily specify the number of `rows` and `columns` for any grid layout.
- **Auto-Resizing**: Crops are automatically resized to a fixed dimension (default: 640x640 pixels) for modern AI models.
- **Automated Organization**: Generates structured output folders (`set1`, `set2`, etc.) to keep your dataset clean.
- **Bulk Processing**: Processes all images within the input directory in a single run.

## 🛠️ Prerequisites

To run this script, you will need **Python 3.x** and the following library:

- **OpenCV (`cv2`)**: Used for high-performance image processing.

Install dependencies via pip:
```bash
pip install opencv-python
```

## 🚀 How to Use

1.  **Prepare your Images**: Place your grid-based photos (e.g., JPEG, PNG) into the `/image-sample` folder.
2.  **Configure the Script**: Open `image-grid-splitter.py` and adjust the variables in the `if __name__ == "__main__":` block:
    - `rows`: Number of vertical grid divisions.
    - `cols`: Number of horizontal grid divisions.
    - `size`: Final output resolution (width/height).
3.  **Run the Script**:
    ```bash
    python image-grid-splitter.py
    ```
4.  **Retrieve Results**: Your cropped and resized images will be saved in the `/result` directory, categorized by their original image sets.

## 📂 Project Structure

```text
├── image-grid-splitter.py   # Core splitting logic
├── image-sample/            # Input folder (put your large photos here)
├── result/                  # Output folder (auto-generated)
└── README.md                # Documentation
```

## 🎯 Use Case: Deep Learning Dataset Preparation
Creating large datasets for deep learning requires thousands of individual images. Instead of manually cropping each object, you can place objects in a grid, take a single high-resolution photo, and use this script to extract all objects perfectly in seconds.

## 🔗 Related Projects

- **[Auto-Image-Labeling](https://github.com/dzakyalfitra/Auto-Image-Labeling)** — Automated bounding box label generation using OpenCV and Otsu's thresholding, with YOLO-format export.
- **[Mosaic-Packed-Generator](https://github.com/dzakyalfitra/Mosaic-Packed-Generator)** — Creates dense, packed mosaics from individual object instances with accurate YOLO label mapping.

---
*Created for efficient dataset engineering.*
