import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tensorflow as tf
from tensorflow import keras    
# Load the dataset
data = pd.read_excel(r'C:\Users\DELL\Downloads\Copy of Marathalli JSP wipro.xlsx')  # Update the path to your dataset
# Display the first few rows of the dataset
print(data.head())  
# Check for missing values
print(data.isnull().sum())
# Fill missing values with the mean of the respective numeric columns
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
# Define features and target variable       
numeric_data = data.select_dtypes(include=[np.number])
X = numeric_data.drop('Degree_Aggregate', axis=1)  # Features
y = numeric_data['Degree_Aggregate']  # Target variable
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a linear regression model   
model = LinearRegression()
model.fit(X_train, y_train)
# Predict on the test set
y_pred = model.predict(X_test)
# Evaluate the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
# Visualize the results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()
