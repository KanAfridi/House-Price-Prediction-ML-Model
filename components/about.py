import streamlit as st

def render_about_page():
    """Render the 'About Project' page."""
    st.title("About the Project")
    st.write(
        """ 
        Working on House Pricing Project has been an invaluable learning experience. I sourced the dataset from Kaggle, providing a rich foundation for hands-on practice. Throughout this project, I meticulously cleaned the data, removing outliers to ensure the highest quality. This process was crucial in preparing the dataset for accurate model training.

        I experimented with various models, applying different techniques to identify the best performer. Through this rigorous testing, I discovered that the XGBRegressor Model yielded the highest accuracy, achieving an impressive 90.50%. This result underscored the importance of model selection and hyperparameter tuning in achieving optimal performance.

        Beyond just technical skills, this project has significantly deepened my understanding of data processing, model evaluation, and the practical challenges in predictive modeling. Each step, from data cleaning to model selection, has enhanced my capabilities and confidence in handling real-world data science tasks. This project has been a pivotal step in my journey to becoming a proficient data scientist.
        """
    )
