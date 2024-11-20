import streamlit as st
import os

def render_eda_page():
    """Render the 'Exploratory Data Analysis' page."""
    st.title("🔍 Exploratory Data Analysis")
    st.write("This section provides insights into the data distribution, relationships, and trends.")
    st.write("---")

    image_files = [
        ("The Scores of Different Algorithms", "different models scores.png"),
        ("The Relationship Between Price and Sqft_living", "relationship between price and sqft_living.png"),
        ("Pie Chart of View", "Pie chart of View.png"),
        ("Distribution Plot of Numerical Columns", "displot before cleaning.png"),
        ("The Distribution of Price After Log Transformation", "the distribution of price after log.png"),
        ("Average Price of Conditions", "avg of condition.png"),
        ("Grade Average Price", "avg price in grade.png"),
        ("Average Price of View", "avg price of View.png"),
        ("Average Price of Waterfront", "avg price of water front.png"),
    ]

    for header, image_file in image_files:
        st.header(header)
        st.image(os.path.join("images", image_file), caption=header)
