import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


#import os
import pickle

# function to load the data from the pickle file
def load_data():
    try:
        with open('Home_prices_data.pkl', 'rb') as file:
            df = pickle.load(file)
            return df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

# function to load the model
def load_model():
    try:
        with open('XGBR__model.pkl', 'rb') as file:
            model = pickle.load(file)
            return model
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

model = load_model()
df = load_data()

