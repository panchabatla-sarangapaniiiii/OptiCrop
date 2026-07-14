"""
OptiCrop Prediction Engine Module
Loads saved models and scalers, validates input data,
performs log transformations, and returns recommendation predictions.
"""

import os
import pickle
import numpy as np
import pandas as pd

from config import MODEL_PATH, SCALER_PATH

def validate_soil_inputs(n, p, k, temp, humidity, ph, rainfall):
    """
    Sanitizes and validates environmental and soil inputs.
    Raises ValueError on negative, invalid, or out-of-bounds parameters.
    """
    # Check nulls/empty
    for name, val in [("Nitrogen", n), ("Phosphorus", p), ("Potassium", k),
                      ("Temperature", temp), ("Humidity", humidity), ("pH", ph), ("Rainfall", rainfall)]:
        if val is None:
            raise ValueError(f"{name} value cannot be empty.")

    # Convert to floats
    try:
        n, p, k = float(n), float(p), float(k)
        temp, humidity, ph, rainfall = float(temp), float(humidity), float(ph), float(rainfall)
    except ValueError:
        raise ValueError("All soil parameters must be numbers.")

    # Negative values validation
    if any(v < 0 for v in [n, p, k, temp, humidity, ph, rainfall]):
        raise ValueError("Soil or environmental parameters cannot be negative.")

    # Specific bounds validation
    if ph < 0 or ph > 14:
        raise ValueError("Soil pH must be between 0 and 14.")

    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity percentage must be between 0 and 100.")

    return n, p, k, temp, humidity, ph, rainfall

def load_prediction_resources():
    """Loads the model and scaler files from disk."""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Model and Scaler assets are not trained or saved yet.")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler

def predict_crop(n, p, k, temp, humidity, ph, rainfall):
    """
    Validates parameters, performs feature scaling,
    and runs prediction using the saved Random Forest model.
    """
    # 1. Validation
    n, p, k, temp, humidity, ph, rainfall = validate_soil_inputs(n, p, k, temp, humidity, ph, rainfall)

    # 2. Load model & scaler
    model, scaler = load_prediction_resources()

    # 3. Log transformation for rainfall (matching training steps)
    rainfall_transformed = np.log1p(rainfall)

    # 4. Form input vector
    input_vector = np.array([[n, p, k, temp, humidity, ph, rainfall_transformed]])

    # 5. Scaling
    input_scaled = scaler.transform(input_vector)

    # 6. Predict Crop
    prediction = model.predict(input_scaled)[0]

    # 7. Probability (Confidence score)
    confidence = 0.95
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_scaled)[0]
        max_idx = np.argmax(probabilities)
        confidence = float(probabilities[max_idx])

    return {
        "crop": prediction,
        "confidence": confidence,
        "parameters": {
            "N": n, "P": p, "K": k,
            "temp": temp, "humidity": humidity,
            "ph": ph, "rainfall": rainfall
        }
    }
