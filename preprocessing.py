"""
OptiCrop Preprocessing Module
Handles data loading, cleaning, duplicate removal, outlier clipping using IQR,
log transformation for highly skewed parameters, and scaling.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(file_path):
    """
    Loads dataset, handles duplicates, handles missing values.
    Returns: cleaned pandas DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset path {file_path} not found.")

    df = pd.read_csv(file_path)

    # 1. Missing Value Handling (Imputation with mean for continuous columns)
    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    for col in features:
        if col in df.columns:
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].mean())

    # 2. Duplicate Removal
    df = df.drop_duplicates()

    return df

def handle_outliers_iqr(df, columns):
    """
    Identifies outliers using Interquartile Range (IQR) and clips them to boundaries.
    """
    df_clipped = df.copy()
    for col in columns:
        if col in df_clipped.columns:
            q1 = df_clipped[col].quantile(0.25)
            q3 = df_clipped[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            # Clipping outliers
            df_clipped[col] = np.clip(df_clipped[col], lower_bound, upper_bound)
    return df_clipped

def apply_log_transformation(df, columns):
    """
    Applies log transformation (log1p) to reduce skewness of specific features (e.g. Rainfall).
    """
    df_transformed = df.copy()
    for col in columns:
        if col in df_transformed.columns:
            df_transformed[col] = np.log1p(df_transformed[col])
    return df_transformed

def preprocess_pipeline(file_path):
    """
    Complete Preprocessing Pipeline.
    Loads, cleans, handles outliers, transforms, and splits data.
    """
    df = load_and_clean_data(file_path)

    # Continuous parameters
    num_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    # IQR outlier clipping
    df = handle_outliers_iqr(df, num_cols)

    # Apply log transformation to highly skewed feature (e.g., Rainfall)
    df = apply_log_transformation(df, ['rainfall'])

    X = df[num_cols]
    y = df['label']

    # Scaling features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, df

import os
if __name__ == "__main__":
    # Test pipeline
    import os
    dataset_path = os.path.join("dataset", "Crop_recommendation.csv")
    if os.path.exists(dataset_path):
        X, y, scaler, df = preprocess_pipeline(dataset_path)
        print(f"Preprocessed features shape: {X.shape}")
        print(f"Labels shape: {y.shape}")
        print("Preprocessing test completed successfully.")
