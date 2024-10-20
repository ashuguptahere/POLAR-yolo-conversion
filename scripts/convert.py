import os
import json

# Define the action-to-class ID mapping
class_mapping = {
    "squat": 0,
    "run": 1,
    "sit": 2,
    "stretch": 3,
    "walk": 4,
    "jump": 5,
    "bendover": 6,
    "stand": 7,
    "lying": 8,
}

# Directory paths
json_dir = "hvnsh7rwz7-1/Annotations/annotations/"  # Directory containing JSON files
output_dir = "converted_data/labels/"  # Directory to save YOLO format files

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over each JSON file
for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        # Read the JSON data
        with open(os.path.join(json_dir, json_file), "r") as f:
            data = json.load(f)

        # Get image dimensions
        img_width = data["width"]
        img_height = data["height"]

        # Get the corresponding YOLO annotation file
        txt_filename = data["filename"].replace(".jpg", ".txt")
        txt_filepath = os.path.join(output_dir, txt_filename)

        with open(txt_filepath, "w") as txt_file:
            # Iterate over each person in the image
            for person in data["persons"]:
                # Get bounding box information
                xmin = person["bndbox"]["xmin"]
                ymin = person["bndbox"]["ymin"]
                xmax = person["bndbox"]["xmax"]
                ymax = person["bndbox"]["ymax"]

                # Convert to YOLO format (normalized)
                x_center = (xmin + xmax) / 2 / img_width
                y_center = (ymin + ymax) / 2 / img_height
                box_width = (xmax - xmin) / img_width
                box_height = (ymax - ymin) / img_height

                # Find the action (class) that has a value of 1
                action_class = None
                for action, value in person["actions"].items():
                    if value == 1:
                        action_class = class_mapping[action]
                        break

                if action_class is not None:
                    # Write the YOLO format annotation
                    txt_file.write(
                        f"{action_class} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n"
                    )

print("Converted POLAR dataset to YOLO format!")
