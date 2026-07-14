"""
OptiCrop Machine Learning Training Module
Trains multiple models: Logistic Regression, Decision Tree, Random Forest, KNN,
computes metrics, compares them, automatically saves the best-performing model
along with its scaler, and writes results to a SQLite database.
"""

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

from preprocessing import preprocess_pipeline
from database import get_db_connection

def train_all_models():
    """
    Trains multiple models, evaluates their performance,
    logs results to SQLite database, and saves the best model.
    """
    dataset_path = os.path.join("dataset", "Crop_recommendation.csv")
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return

    print("Step 1: Running Preprocessing Pipeline...")
    X_scaled, y, scaler, df = preprocess_pipeline(dataset_path)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Define models to train
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "K Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
    }

    results = {}
    best_model_name = None
    best_f1 = 0.0
    best_model_obj = None

    print("\nStep 2: Training and Evaluating Supervised Models...")
    for name, model in models.items():
        # Fit model
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')

        print(f"[{name}] Accuracy: {acc:.4f} | F1-Score: {f1:.4f}")

        results[name] = {
            "model_obj": model,
            "accuracy": acc,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "report": classification_report(y_test, y_pred)
        }

        # Track best model
        if f1 > best_f1:
            best_f1 = f1
            best_model_name = name
            best_model_obj = model

    # Unsupervised Model: K-Means Clustering (for demonstration/analysis)
    print("\nStep 3: Training Unsupervised K-Means model for cluster profiling...")
    unique_crops = len(y.unique())
    kmeans = KMeans(n_clusters=unique_crops, random_state=42, n_init='auto')
    kmeans.fit(X_scaled)
    # Logging clustering outcome
    print(f"[K-Means Clustering] Completed fitting {unique_crops} clusters.")

    # Save best supervised model and scaler
    print(f"\nStep 4: Saving Best Supervised Model: {best_model_name}...")
    with open("model.pkl", "wb") as f:
        pickle.dump(best_model_obj, f)

    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    # Save to models/ folder as fallback/archive
    with open(os.path.join("models", "best_model.pkl"), "wb") as f:
        pickle.dump(best_model_obj, f)
    with open(os.path.join("models", "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)

    # Log model metrics into database
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Log training runs
        for name, metrics in results.items():
            cursor.execute("""
            INSERT INTO MLModel (name, accuracy, precision_score, recall_score, f1_score, parameters, saved_path)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (
                name,
                float(metrics["accuracy"]),
                float(metrics["precision"]),
                float(metrics["recall"]),
                float(metrics["f1_score"]),
                str(metrics["model_obj"].get_params() if hasattr(metrics["model_obj"], "get_params") else "N/A"),
                "model.pkl" if name == best_model_name else "N/A"
            ))

        conn.commit()
        conn.close()
        print("Model metadata successfully saved to SQLite Database.")
    except Exception as e:
        print(f"Error logging to database: {e}")

    print("\nTraining workflow executed perfectly!")

if __name__ == "__main__":
    train_all_models()
