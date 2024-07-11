import pandas as pd
from typing import List

data = "./melb_data.csv"


df = pd.read_csv(data)

print(df.describe())

# View columns
# print(df.columns)

# select a specific column

print(df.Rooms)
