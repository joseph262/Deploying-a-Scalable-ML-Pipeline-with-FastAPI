import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics

# Assuming that the process_data function processes the data and returns numpy arrays
# and train_model trains a RandomForestClassifier

def load_dummy_data():
    # Create or load a small amount of data for testing purposes
    data = {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": ["A", "B", "C", "D", "E"],
        "target": [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_ml_function_return_types():
    """
    Test if the ML functions return data of the expected type.
    """
    data = load_dummy_data()
    X, y, _, _ = process_data(data, categorical_features=["feature2"], label="target")
    
    # Testing return type of process_data function
    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(y, np.ndarray), "y should be a numpy array"

    model = train_model(X, y)
    
    # Testing return type of train_model function
    assert isinstance(model, RandomForestClassifier), "Model should be a RandomForestClassifier instance"

def test_ml_model_algorithm():
    """
    Test if the ML model uses the expected algorithm.
    """
    data = load_dummy_data()
    X, y, _, _ = process_data(data, categorical_features=["feature2"], label="target")
    model = train_model(X, y)

    # Check if the model is indeed a RandomForestClassifier
    assert isinstance(model, RandomForestClassifier), "The trained model should be a RandomForestClassifier"

def test_dataset_size_and_type():
    """
    Test if the training and test datasets have the expected size or data type.
    """
    data = load_dummy_data()
    X, y, _, _ = process_data(data, categorical_features=["feature2"], label="target")

    # Check the size of the datasets
    assert X.shape[0] == y.shape[0], "X and y should have the same number of rows"

    # Check the type of the datasets
    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(y, np.ndarray), "y should be a numpy array"