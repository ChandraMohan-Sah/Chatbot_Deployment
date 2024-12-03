import os
from ultralytics import YOLO

# Load YOLO model
MODEL_PATH = os.path.join(os.getcwd(), 'best.pt')
model = YOLO(MODEL_PATH)

def run_inference(image_path, output_dir):
    """
    Runs YOLO inference on the given image and saves the result.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory to save the result image.

    Returns:
        str: Path to the result image.
        list: Detected objects with labels and confidence scores.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Run YOLO inference
    results = model([image_path])
    result_image_path = os.path.join(output_dir, f"result_{os.path.basename(image_path)}")
    results[0].save(filename=result_image_path)

    # Extract detected objects (label and confidence)
    detected_objects = []
    for box in results[0].boxes:
        label = box.data[0][-1]  # Label index
        score = box.data[0][-2]  # Confidence score
        detected_objects.append({
            'label': model.names[int(label)],
            'score': f"{score:.2f}"
        })

    return result_image_path, detected_objects
