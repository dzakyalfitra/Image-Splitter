import cv2
import os

def crop_objects(image_path, output_dir, set_id, rows=6, cols=9, size=640):
    """
    Crop multiple objects arranged in a grid (rows x cols) into individual images.

    Args:
        image_path (str): Path to the original photo containing objects.
        output_dir (str): Base folder to save cropped images.
        set_id (int/str): Unique ID for this full image (e.g., 1, 2, 3...).
        rows (int): Number of rows of objects.
        cols (int): Number of columns of objects.
        size (int): Output crop size (square).
    """
    # Read original image
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Calculate object crop size (assuming grid layout)
    object_h = h // rows
    object_w = w // cols

    # Create output folder for this set
    set_folder = os.path.join(output_dir, f"set{set_id}")
    os.makedirs(set_folder, exist_ok=True)

    object_id = 1
    for r in range(rows):
        for c in range(cols):
            # Crop object
            y1, y2 = r * object_h, (r + 1) * object_h
            x1, x2 = c * object_w, (c + 1) * object_w
            object_crop = img[y1:y2, x1:x2]

            # Resize to fixed size (e.g., 640x640)
            object_resized = cv2.resize(object_crop, (size, size))

            # Unique filename (setID + objectID)
            filename = f"set{set_id}_object{object_id:02d}.jpg"
            filepath = os.path.join(set_folder, filename)

            cv2.imwrite(filepath, object_resized)
            object_id += 1

    print(f"[INFO] Saved {object_id-1} objects to {set_folder}")

# ========= Usage ==========
if __name__ == "__main__":
    input_images = "./image-sample/"    # folder containing your original multiple object photos
    output_dataset = "result"           # where cropped images will be saved

    os.makedirs(output_dataset, exist_ok=True)

    # Loop through all original full images
    for idx, filename in enumerate(sorted(os.listdir(input_images)), start=1):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(input_images, filename)
            crop_objects(image_path, 
                       output_dataset, 
                       set_id=idx, 
                       rows=6,      # set the image rows, default= 6
                       cols=9,      # set the image columns, default=9
                       size=640)    # set the image size, default 640 pixels