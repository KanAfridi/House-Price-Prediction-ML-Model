import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import pandas as pd
import numpy as np
from utils.load_pickle import load_model
from components.user_input_templete import make_prediction

# Decorate the user_input function to make it a fixture
@pytest.fixture
def user_input():
    return {
        'bedrooms': 3,
        'sqft_living': 2500,
        'sqft_lot': 3000,
        'waterfront': 1,
        'view': 4,
        'condition': 3,
        'grade': 8,
        'yr_built': 1920,
        'lat': 47.1559,
        'long': -122.519,
        'sqft_living15': 2300
    }

# Test function to verify the model
def test_prediction(user_input):
    model = load_model()
    df = pd.DataFrame([user_input])  # This ensures it's treated as a 2D array
    prediction = make_prediction(user_input, model) # Make a prediction using the loaded model and user input data
    expected_prediction = model.predict(df)

    # Verify that the prediction is a positive number
    assert prediction == np.exp(expected_prediction)[0]
    print("All tests passed! Congratulations")   

