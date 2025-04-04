import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Get Database URL from Environment
DATABASE_URL = "mysql+pymysql://root:Kutti%402004@localhost:3306/tanzura_db"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True)

# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class for Models
Base = declarative_base()

# Function to initialize database tables
def init_db():
    from models.models import Base  # Import here to avoid circular imports
    Base.metadata.create_all(bind=engine)
