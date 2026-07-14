"""
OptiCrop Configuration Module
Defines system-wide constants, database paths, and ML parameters.
"""

import os

# Base directory of the application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask configuration
SECRET_KEY = os.environ.get("SECRET_KEY", "opti-crop-super-secret-key-2026")
DEBUG = True

# Database configuration
DATABASE_PATH = os.path.join(BASE_DIR, "opticrop.db")

# Model configuration
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Ensure models directory exists
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
