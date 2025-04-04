import cv2 
import numpy as np
import torch
from ultralytics import YOLO
import os
import torch.serialization

# Allow YOLO model class for safe serialization
torch.serialization.add_safe_globals(["DetectionModel"])  # Ensure compatibility

# Define Model Path
MODEL_PATH = "services/yolo_model.pt"

# Ensure the model file exists before loading
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please check the path.")

# Load YOLO Model (weights only)
try:
    model = YOLO(MODEL_PATH, weights_only=True)  # Load only weights
except Exception as e:
    raise RuntimeError(f"Error loading YOLO model: {str(e)}")

def detect_microplastics(image_path):
    """
    Detects microplastics in a given water sample image using a YOLO model.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        dict: Detection results including risk level, confidence score, and filtration recommendations.
    """
    # Validate input image path
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}. Please check the path.")

    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Error loading image from {image_path}. Ensure the file is a valid image.")

    # Perform detection using YOLO
    try:
        results = model.predict(img)
    except Exception as e:
        raise RuntimeError(f"Error during model inference: {str(e)}")

    # Extract bounding boxes & confidence scores
    detections = results[0].boxes.data.cpu().numpy() if results and len(results[0].boxes) > 0 else np.array([])

    # If no microplastics are detected, return "Safe" classification
    if detections.size == 0:
        return {
            "risk_level": "Safe",
            "confidence": 0.0,
            "water_quality_score": 100,
            "filtration_recommendations": "No filtration needed"
        }

    # Calculate Average Confidence Score
    avg_confidence = np.mean(detections[:, 4]) * 100  # Confidence is stored at index 4

    # Risk Level Classification
    if avg_confidence > 80:
        risk_level = "High"
        water_quality_score = 30
        filtration_recommendations = "Use Reverse Osmosis (RO) & Activated Carbon Filtration"
    elif avg_confidence > 50:
        risk_level = "Moderate"
        water_quality_score = 60
        filtration_recommendations = "Use Carbon Filtration & UV Purification"
    else:
        risk_level = "Low"
        water_quality_score = 85
        filtration_recommendations = "Basic Filtration (Sand & Activated Carbon)"

    return {
        "risk_level": risk_level,
        "confidence": round(avg_confidence, 2),
        "water_quality_score": water_quality_score,
        "filtration_recommendations": filtration_recommendations
    }
