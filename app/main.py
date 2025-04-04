import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db  # ✅ Correct import
from routes import auth, detection
import logging

# Initialize FastAPI App
app = FastAPI(
    title="Tanzura - AI-Powered Microplastic Detection",
    description=(
        "Tanzura is an advanced AI-powered platform designed to detect microplastics in water samples. "
        "Using cutting-edge YOLO and OpenCV-based image analysis, it provides accurate risk assessments, "
        "water quality scores, and recommendations for filtration methods. This tool is built for individuals, "
        "researchers, and government agencies to ensure safe drinking water."
    ),
    version="1.0.0",
)

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Enable CORS for Frontend Compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(auth.router)
app.include_router(detection.router)

# Database Initialization on Startup
@app.on_event("startup")
def startup_event():
    logger.info("🚀 Tanzura Server is starting...")
    logger.info("📊 Setting up the database and creating tables if they don't exist.")
    init_db()  # ✅ Calling the correct function
    logger.info("✅ Database setup complete.")
    logger.info("🔗 Tanzura API is now live at http://localhost:8000")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("🛑 Shutting down Tanzura Server...")

# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "🌊 Welcome to Tanzura - AI-Powered Microplastic Detection! 🌊",
        "description": (
            "Tanzura is an AI-driven solution for detecting microplastic contamination in water samples. "
            "Upload images of water samples, and our advanced YOLO model will analyze and classify contamination levels. "
            "Get detailed risk assessments, water quality scores, and personalized filtration recommendations."
        ),
        "features": [
            "🔬 AI-based Microplastic Detection",
            "📊 Water Quality Score (0-100%)",
            "🚦 Risk Classification (Safe, Moderate, High)",
            "🛡️ Filtration Recommendations (RO, Activated Carbon, etc.)",
            "📁 Secure File Upload System",
            "🔑 User Authentication & Role-Based Dashboards",
            "📡 Real-Time Insights for Researchers & Government Agencies"
        ],
        "api_endpoints": {
            "User Authentication": "/auth/",
            "Microplastic Detection": "/detection/",
        },
        "docs": "Access API documentation at /docs or /redoc",
        "status": "✅ Tanzura API is running smoothly!"
    }

# Run Server (Only if executed directly)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
