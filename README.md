# 🏠 House-Price-Prediction-ML

## 📊 House Pricing Prediction Model

This repository contains the machine learning model for predicting house prices based on various features such as the number of bedrooms, bathrooms, square footage, and other relevant features. The model utilizes data preprocessing techniques, feature engineering, and hyperparameter tuning to achieve high accuracy in price predictions.

This project is aimed at predicting house prices using historical data that includes various features such as the number of bedrooms, bathrooms, square footage, and other characteristics of the properties. The main objective is to provide accurate house price predictions, which can assist real estate professionals, buyers, and sellers in making informed decisions.

### Webapp Link:  [House Price Prediction Webapp](https://kanafridi-house-price-prediction-ml-model-srcapp-pmuvq7.streamlit.app/)

## 🛠️ Software and Tools Requirements

Before running this project, make sure you have the following tools and software installed:

- **[GitHub Account](https://github.com/)** - To manage the repository and collaborate on the project. 🌐
- **[VS Code IDE](https://code.visualstudio.com/)** - The recommended code editor for development. 💻
- **[Git CLI](https://git-scm.com/)** - For version control and managing repositories. ⚙️
- **[Python 3.x](https://www.python.org/downloads/)** - Make sure you have Python 3.x installed to run the project. 🐍
- **[Streamlit](https://streamlit.io/)** - To deploy and run the machine learning model as a web application. 🚀
- **[XGBoost](https://xgboost.readthedocs.io/en/stable/)** - For implementing the gradient boosting model used for house price prediction. 🌱

### 🚀 Future Deployment
- This project will soon be deployed to the web for public access. 🌍

## 📑 Table of Contents
- [Data Preprocessing](#data-preprocessing)
- [Model Selection](#model-selection)
- [Feature Importance and Optimization](#feature-importance-and-optimization)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Model Evaluation](#model-evaluation)
- [Saving the Model](#saving-the-model)
- [Setup and Usage](#setup-and-usage)
- [File Structure](#file-structure)
- [Conclusion](#conclusion) 
- [Directory Structure](#directory-structure) 
- [Key Points of the Project](##Key-Points-of-the-Project) 

## 🧹 Data Preprocessing

The dataset initially contained 18 columns, many of which had outliers or missing values. Here's how I handled the data:

1. **Outlier Removal:** 
   - High price values and extremely low prices were filtered out, as they could significantly distort the model’s performance. 
   - I used a range filter to remove values outside an acceptable range, based on domain knowledge.
   
2. **Price Transformation:**
   - The `Price` column had a skewed distribution, so I applied various transformations, such as taking the square root. Ultimately, the log transformation of the price column provided the best normalization.

3. **Feature Engineering:**
   - Features like bedrooms, bathrooms, and square footage were used as primary inputs.
   - Other columns such as the age of the house, neighborhood, and parking facilities were also considered.

4. **Splitting the Data:**
   - The dataset was split into training and testing subsets to evaluate model performance effectively.

## 🤖 Model Selection

Several algorithms were tested to predict house prices, including:
- Linear Regression
- Decision Trees
- Random Forest
- XGBRegressor
- GradientBoostingRegressor


After evaluating the performance of all models, **XGBRegressor** was found to be the best-performing model, achieving alomst an impressive **90% accuracy**. 🏅

## Score Of Chossen Model😍
### **XGBRegressor**
- **Accuracy: 0.894**
- **MSE: 0.029**
- **MAE: 0.121**
- **RMSE: 0.171**


## 🔍 Feature Importance and Optimization

To optimize the model and enhance performance, I conducted feature importance analysis using the XGBRegressor model. Here’s the approach I used:

1. **Feature Selection:**
   - I iteratively removed one feature at a time to observe its impact on model performance. 
   - Five columns were found to have a minimal effect on the accuracy (only 0.006% change), so they were removed to reduce complexity.
   
2. **Model Simplification:**
   - After removing the less significant features, the model was trained with the remaining 10 important features. Notably, the number of bedrooms, despite being important for humans, had minimal effect on the model’s accuracy, so I chose to retain it for user simplicity.

## 🔧 Hyperparameter Tuning

I initially applied **RandomizedSearchCV** to tune hyperparameters, but it didn’t provide substantial improvement. So, I used manual adjustments, testing different parameters to see which ones provided optimal results. While the improvements were minimal, the final configuration was selected to achieve the best results.

## 🏆 Model Evaluation

The model was evaluated using various metrics such as:
- **Mean Absolute Error (MAE)**: 📉
- **Mean Squared Error (MSE)**: 📉
- **Root Mean Squared Error (RMSE)**: 📉


The XGBRegressor performed excellently with minimal error, making it suitable for real-world deployment. 🎯

## 💾 Saving the Model

Once the model was trained, I saved the final model and preprocessed data using **Pickle** for future use in a web application. This allows for easy loading of the trained model and data into a Streamlit app for real-time predictions. 🔄

## 📁 Directory Structure

```
|-- price-prediction-prac/
|-- .github
  |-- workflows
    |-- main.yml
|-- components
  |-- about.py
  |-- eda.py
  |-- user_input_templete.py
  |-- __init__.py
|-- images
  |-- avg of condition.png
  |-- avg price in grade.png
  |-- Etc
|-- src
  |-- app.py
  |-- __init__.py
|-- tests
  |-- test.py
  |-- __init__.py
|-- utils
  |-- load_pickle.py
  |-- __init__.py
|-- XGBR__model.pkl
|-- Home_prices_data.pkl
|-- .gitattributes
|-- LICENSE
|-- myvenv
|-- README.md
|-- requirements.txt
|-- .gitignore
```


## ✨ Key Points of the Project

- **Data Preprocessing**: 
  - Cleaned the dataset by removing outliers, including houses with extremely high prices.
  - Applied techniques like square root and log transformations to normalize the price column.
  
- **Modeling**: 
  - Split the data into training and testing sets.
  - Tried several algorithms, with XGBoostRegressor achieving the best results (90% accuracy).
  - Conducted feature importance analysis and removed less impactful columns.
  
- **Hyperparameter Tuning**: 
  - Applied hyperparameter tuning, but custom adjustments showed minimal improvement over default settings.
  
- **Feature Selection**: 
  - Used feature importance to drop columns with minimal impact on accuracy.
  - Retained essential features like bathrooms and bedrooms for a simpler user input interface in the Streamlit app.

- **Model Saving**: 
  - Saved the trained model using pickle for future use and deployment.

- **Next Steps**: 
  - Planning to deploy the model as a web application using Streamlit. 🚀
  - Will improve the web app interface for better user experience. 🎨


