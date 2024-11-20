
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
from utils.load_pickle import load_data, load_model
from components.about import render_about_page
from components.user_input_templete import render_prediction_page
from components.eda import render_eda_page

# Load data and model
model = load_model()
df = load_data()

# Sidebar for navigation
st.sidebar.title("Navigation Bar")
page = st.sidebar.radio("Go to", ["About Project", "Model Prediction", "Exploratory Data Analysis"])

# Render the selected page
if page == "About Project":
    render_about_page()
elif page == "Model Prediction":
    render_prediction_page(df, model)
elif page == "Exploratory Data Analysis":
    render_eda_page()

