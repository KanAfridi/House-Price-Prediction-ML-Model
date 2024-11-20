
import sys
import os
# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import numpy as np
from utils.load_pickle import df, model



# This is the template for streamlit model
def get_user_input(df):
    """Get user inputs for the prediction model."""
    col1, col2, col3 = st.columns(3)

    with col1:
        sqft_living = st.slider('🛋️ Squarefeet Living', int(df['sqft_living'].min()), int(df['sqft_living'].max()))
        grade = st.selectbox('🏅 Grade', df['grade'].sort_values().unique())
        bedrooms = st.selectbox('🛏️ Bedrooms', df['bedrooms'].sort_values().unique())

    with col2:
        lat = st.slider('🌎 Latitude', float(df['lat'].min()), float(df['lat'].max()))
        long = st.slider('🌍 Longitude', float(df['long'].min()), float(df['long'].max()))
        sqft_living15 = st.slider('🛋️ Sqft Living (Nearby)', int(df['sqft_living15'].min()), int(df['sqft_living15'].max()))

    with col3:
        view = st.selectbox('👀 House View', df['view'].sort_values().unique())
        condition = st.selectbox('🔍 Condition', df['condition'].sort_values().unique())
        waterfront = st.radio('🌊 Waterfront', ['No', 'Yes'], horizontal=True)
        waterfront = 1 if waterfront == 'Yes' else 0

    # Additional inputs
    yr_built = st.selectbox('📅 Year Built', df['yr_built'].sort_values().unique())
    sqft_lot = st.number_input("🏡 Lot Size (Sqft)", value=int(df['sqft_lot'].median()), step=100)

    # This input is used to select userinput into there perfect match column names because i train the model with features name
    user_input = {
                'bedrooms': bedrooms,
                'sqft_living': sqft_living,
                'sqft_lot': sqft_lot,
                'waterfront': waterfront,
                'view': view,
                'condition': condition,
                'grade': grade,
                'yr_built': yr_built,
                'lat': lat,
                'long': long,
                'sqft_living15': sqft_living15
                }
    return  user_input

# This is the function of a model to predict the outcome of the user input
def make_prediction(input_data, model):
    """Make predictions using the input data and trained model."""
    query_data = pd.DataFrame([input_data])
    prediction = model.predict(query_data)
    return np.exp(prediction)[0]  # Assuming log-transformed target


# this function will render the main prediction page
def render_prediction_page(input_data, model):
    """Render the main prediction page."""
    st.title("🏠 Predict House Price")
    st.write("Adjust the sliders and select options below to predict the price of the house.")
    st.write("---")

    # Get user inputs
    user_input = get_user_input(input_data)

    # Prediction and logging
    if st.button('💡 Predict Price'):
        predicted_price = make_prediction(user_input, model)
        st.success(f"### 🎉 The predicted House Price: **${predicted_price:,.2f}**")
        st.balloons()

        #log_prediction(user_input, predicted_price)

# Load data and model
def main():
    render_prediction_page(df, model)

# Run the app
if __name__ == "__main__":
    main()

