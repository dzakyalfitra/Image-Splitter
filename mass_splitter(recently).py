import cv2
import os

def crop_beans(image_path, output_dir, set_id, rows=6, cols=9, size=640):
    """
    Crop coffee beans arranged in a grid (rows x cols) into individual images.

    Args:
        image_path (str): Path to the original photo containing beans.
        output_dir (str): Base folder to save cropped images.
        set_id (int/str): Unique ID for this full image (e.g., 1, 2, 3...).
        rows (int): Number of rows of beans.
        cols (int): Number of columns of beans.
        size (int): Output crop size (square).
    """
    # Read original image
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Calculate bean crop size (assuming grid layout)
    bean_h = h // rows
    bean_w = w // cols

    # Create output folder for this set
    set_folder = os.path.join(output_dir, f"set{set_id}")
    os.makedirs(set_folder, exist_ok=True)

    bean_id = 1
    for r in range(rows):
        for c in range(cols):
            # Crop bean
            y1, y2 = r * bean_h, (r + 1) * bean_h
            x1, x2 = c * bean_w, (c + 1) * bean_w
            bean_crop = img[y1:y2, x1:x2]

            # Resize to fixed size (e.g., 640x640)
            bean_resized = cv2.resize(bean_crop, (size, size))

            # Unique filename (setID + beanID)
            filename = f"set{set_id}_bean{bean_id:02d}.jpg"
            filepath = os.path.join(set_folder, filename)

            cv2.imwrite(filepath, bean_resized)
            bean_id += 1

    print(f"[INFO] Saved {bean_id-1} beans to {set_folder}")


# ===== Example usage =====
if __name__ == "__main__":
    input_images = "D:/CoffeeBeansDataset/capture/full_image_23-9-25/right"     # folder containing your original 54-bean photos
    output_dataset = "selected_beans_dataset_0"  # where cropped beans will be saved

    os.makedirs(output_dataset, exist_ok=True)

    # Loop through all original full images
    for idx, filename in enumerate(sorted(os.listdir(input_images)), start=1):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(input_images, filename)
            crop_beans(image_path, output_dataset, set_id=idx+39, rows=6, cols=9, size=640)
