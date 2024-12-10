import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Get database connection URL form env
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    # raise ValueError("Fehler: Die Umgebungsvariable SQLALCHEMY_DATABASE_URL ist nicht gesetzt.")
    SQLALCHEMY_DATABASE_URL = "postgresql://db_user:db_password@localhost:5432/budget_planner"
# Create database engine for connection
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# SessionLocal for managing current sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for models
Base = declarative_base()
