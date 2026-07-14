"""
OptiCrop Database Operations Module
Manages SQLite connection, table initialization, and relational records.
"""

import sqlite3
import os
from config import DATABASE_PATH

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Initializes the SQLite database with strict relational schemas.
    Creates tables: User, SoilData, Crop, Dataset, MLModel, Prediction, Report
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. User Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'Farmer',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. SoilData Table (Laboratory Parameters)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SoilData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nitrogen REAL NOT NULL,
        phosphorus REAL NOT NULL,
        potassium REAL NOT NULL,
        temperature REAL NOT NULL,
        humidity REAL NOT NULL,
        ph REAL NOT NULL,
        rainfall REAL NOT NULL,
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Crop Table (Information regarding crops)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Crop (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT UNIQUE NOT NULL,
        common_name TEXT NOT NULL,
        scientific_name TEXT NOT NULL,
        optimal_temp_range TEXT,
        optimal_ph_range TEXT,
        water_requirement TEXT,
        market_value_usd_acre REAL
    );
    """)

    # 4. Dataset Table (Tracking dataset loads & versions)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dataset (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        version_label TEXT NOT NULL,
        file_path TEXT NOT NULL,
        row_count INTEGER,
        feature_count INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. MLModel Table (Information regarding trained models and metrics)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MLModel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        accuracy REAL NOT NULL,
        precision_score REAL NOT NULL,
        recall_score REAL NOT NULL,
        f1_score REAL NOT NULL,
        parameters TEXT,
        saved_path TEXT,
        trained_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 6. Prediction Table (Records actual model runs)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prediction (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        soil_data_id INTEGER NOT NULL,
        recommended_crop_id INTEGER,
        confidence REAL,
        predicted_crop_label TEXT NOT NULL,
        model_used_id INTEGER,
        prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User (id) ON DELETE SET NULL,
        FOREIGN KEY (soil_data_id) REFERENCES SoilData (id) ON DELETE CASCADE,
        FOREIGN KEY (recommended_crop_id) REFERENCES Crop (id) ON DELETE SET NULL,
        FOREIGN KEY (model_used_id) REFERENCES MLModel (id) ON DELETE SET NULL
    );
    """)

    # 7. Report Table (PDF Reports generated)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Report (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prediction_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        recommendations TEXT,
        generated_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (prediction_id) REFERENCES Prediction (id) ON DELETE CASCADE
    );
    """)

    # Seed default crops for high-fidelity information
    crops_seed = [
        ('rice', 'Rice', 'Oryza sativa', '20-27 C', '5.5-7.5', 'High', 2450.0),
        ('maize', 'Maize', 'Zea mays', '18-27 C', '5.5-7.0', 'Medium', 1800.0),
        ('chickpea', 'Chickpea', 'Cicer arietinum', '15-25 C', '6.0-7.0', 'Low', 1200.0),
        ('kidneybeans', 'Kidney Beans', 'Phaseolus vulgaris', '15-25 C', '5.5-6.5', 'Medium', 1500.0),
        ('pigeonpeas', 'Pigeon Peas', 'Cajanus cajan', '20-30 C', '5.0-7.0', 'Low', 1350.0),
        ('mothbeans', 'Moth Beans', 'Vigna aconitifolia', '25-35 C', '5.5-7.5', 'Low', 1100.0),
        ('banana', 'Banana', 'Musa acuminata', '20-30 C', '6.0-7.5', 'High', 3200.0),
        ('mango', 'Mango', 'Mangifera indica', '25-35 C', '5.5-7.0', 'Low', 4500.0),
        ('grapes', 'Grapes', 'Vitis vinifera', '15-25 C', '5.5-6.5', 'Medium', 6000.0),
        ('watermelon', 'Watermelon', 'Citrullus lanatus', '22-30 C', '6.0-7.0', 'Medium', 2100.0),
        ('apple', 'Apple', 'Malus domestica', '15-25 C', '5.5-6.5', 'Medium', 5200.0),
        ('orange', 'Orange', 'Citrus sinensis', '15-30 C', '5.5-7.0', 'Medium', 3800.0),
        ('papaya', 'Papaya', 'Carica papaya', '22-30 C', '6.0-6.5', 'Medium', 2900.0),
        ('coconut', 'Coconut', 'Cocos nucifera', '25-35 C', '5.0-8.0', 'High', 3500.0),
        ('cotton', 'Cotton', 'Gossypium', '20-30 C', '5.5-6.5', 'Medium', 1950.0),
        ('jute', 'Jute', 'Corchorus', '24-35 C', '6.0-7.5', 'High', 1750.0),
        ('coffee', 'Coffee', 'Coffea', '15-25 C', '5.5-6.5', 'High', 5500.0),
    ]

    for crop in crops_seed:
        cursor.execute("""
        INSERT OR IGNORE INTO Crop (label, common_name, scientific_name, optimal_temp_range, optimal_ph_range, water_requirement, market_value_usd_acre)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """, crop)

    # Seed default user
    cursor.execute("""
    INSERT OR IGNORE INTO User (name, email, password_hash, role)
    VALUES ('Dr. Sarah Jenkins', 'sarah.jenkins@opticrop.org', 'pbkdf2:sha256:default_hash_for_testing_123', 'Researcher');
    """)

    conn.commit()
    conn.close()
    print("SQLite Database initialized successfully.")

if __name__ == "__main__":
    init_db()
