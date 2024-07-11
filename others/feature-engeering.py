import pandas as pd
from typing import List
from sklearn.tree import DecisionTreeRegressor 


data = "./melb_data.csv"


df = pd.read_csv(data)

print(df.describe())

# View columns
# print(df.columns)

# select a specific column using the dot notation 
# print(df.Rooms)
# print(df['Rooms'])

print("======  Selecting The Prediction Target ======")
y = df.Price
# print(y)
y.to_csv('prediction_data.csv', index=False)


""" Choosing Features" The columns used to make predictions" """
feature_columns = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

print("===== Feature columns ======= ")
X = df[feature_columns]
# print(X)

# saving featured data into a csv file 
X.to_csv('featured_data.csv', index=False)

print("=====  Describing Feature columns ======= ")
# print(X.describe())
print(X.head(4))
print(X.tail(5))

# Building Your Model
""" 
The steps to building and using a model are:
- Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
- Fit: Capture patterns from provided data. This is the heart of modeling.
- Predict: Just what it sounds like
- Evaluate: Determine how accurate the model's predictions are.
"""
print("===========  Building Your Model  =============")
# scikit-learn is used in building the models 
df_model = DecisionTreeRegressor(random_state=1)

df_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(df_model.predict(X.head()))

print(df_model.predict(X.head(1)))