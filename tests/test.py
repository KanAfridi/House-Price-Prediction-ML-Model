

import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest
import pandas as pd
from utils.load_pickle import load_model
from components.user_input_templete import make_prediction

# Load the model
model = load_model()

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



def test_predicts(user_input):
    # Load the model
    model = load_model()
    
    input_df = pd.DataFrame([user_input])
    
    # Predict the user input
    prediction = make_prediction(user_input, model)  # Prediction from tested function
    test_predictions = model.predict(input_df)       # Direct model prediction
    
    # Assert that the predictions match (with numerical tolerance)
    assert np.isclose(prediction, np.exp(test_predictions)[0], atol=1e-6) # This one is better option
    #assert prediction == np.exp(test_predictions)[0]
    print("All tests passed! Congratulations")   

# Run with pytest
# Save this in a test file and run using: pytest <test_file_name>.py
