import os
from ultralytics import YOLO

# Get current working directory
cwd = os.getcwd()

# Load a COCO-pretrained YOLO model
model = YOLO("yolo11x.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(
    data=f"{cwd}/dataset/data.yaml",
    epochs=300,
    imgsz=640,
    device=0,
    batch=16,
)
