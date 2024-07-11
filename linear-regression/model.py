# MACHINE LEARNING GUIDE OR STEPS 
# GUESTION ==> DATA GATHERING ==> CLEAN ==> EXPLORE ==> MODEL 

import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# getting the data
data = pd.read_csv("./data.csv")

# describing the data
# print(data.describe())

X = df(data=data, columns=["prod_budget"])
y = df(data=data, columns=["world_gross"])


# scatter plot 
plt.figure(figsize=(10,6))
plt.scatter(X, y, alpha=0.3) # alpha=0.3 makes the point transparent 
plt.title("Film Cost vs Global Revenue ")
plt.xlabel("Production Cost $")
plt.ylabel("Worldwide Gross ")
plt.ylim(0, 3_000_000_000) # reduces the scale and makes it fit well on the axis 
plt.xlim(0, 450_000_000)


plt.savefig('scatter-plot.png')

# plt.show()

# BUILDING THE LINEAR REGRESSION MODEL 
# y = mx + c
# In machine learning the intercept and slope is referred to as parameters 
# In ML  intercept slope 
# ho(X) =  O0 +  O1x

# CREATING A LINEAR REGRESSION  
regression = LinearRegression()

# FITTING THE MODEL 
regression.fit(X, y)

regression_coefficient  = regression.coef_[0][0]

regression_intercept = regression.intercept_[0]
print({"coefficient": regression_coefficient, "intercept": regression_intercept})


# PLOTTING THE LINE ON THE CHART 
plt.figure(figsize=(10,6))
plt.scatter(X, y,  color="orange", alpha=0.3) # alpha=0.3 makes the point transparent 
plt.plot(X, regression.predict(X), linewidth=4)
plt.title("Film Cost vs Global Revenue ")
plt.xlabel("Production Cost $")
plt.ylabel("Worldwide Gross ")
plt.ylim(0, 3_000_000_000) # reduces the scale and makes it fit well on the axis 
plt.xlim(0, 450_000_000)
plt.savefig('scatter-plot-with-line.png')

# EVALUATE AND ANALYZE THE MODEL 
# Since coefficient/gradient it 3.11 means there is a +ve relationship between budget and revenue which also means that for every dollar spent there is a revenue of 3.11 

# Interpreting the intercept 
# Means a movie with a budget of zero will loose over 7million dollars which is unrealistic 

# CHECKING FOR THE R-SQUARE 
r_square = regression.score(X, y)

# Explains the amount of variation in film revenue explained by the film budget. which is 55% and thats very good.

print({"r-square": r_square})