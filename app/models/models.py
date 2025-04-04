from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    """ User Model for authentication """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: One user can upload multiple images
    uploads = relationship("Upload", back_populates="user")


class Upload(Base):
    """ Upload Model for storing uploaded images & results """
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_path = Column(String(255), nullable=False)  # Stores file path of uploaded image
    detected_particles = Column(Integer, nullable=False)  # Count of detected microplastic particles
    confidence_score = Column(Float, nullable=False)  # AI model confidence percentage
    risk_level = Column(String(20), nullable=False)  # Risk classification (Low, Moderate, High)
    water_quality_score = Column(Float, nullable=False)  # Water quality (0-100 scale)
    recommended_filters = Column(String(255), nullable=False)  # Recommended filtration techniques
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: Each upload belongs to a user
    user = relationship("User", back_populates="uploads")
