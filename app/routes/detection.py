from fastapi import APIRouter, UploadFile, File, HTTPException
import cv2
import numpy as np
import os
from services.ai_model import detect_microplastics

router = APIRouter(prefix="/detect", tags=["Detection"])

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# API Endpoint for Image Upload & Microplastic Detection
@router.post("/")
async def detect_microplastics_endpoint(file: UploadFile = File(...)):
    try:
        # Read Image
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Perform AI Detection
        detection_results = detect_microplastics(file_path)

        return {
            "filename": file.filename,
            "risk_level": detection_results["risk_level"],
            "confidence": detection_results["confidence"],
            "water_quality_score": detection_results["water_quality_score"],
            "filtration_recommendations": detection_results["filtration_recommendations"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
