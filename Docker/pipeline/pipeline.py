import sys

import pandas as pd

# print('arguments',sys.argv)

# supplying commad line input atgv value stats from 0
month = int(sys.argv[1]) # supplying commad line input atgv value stats from 0

# Creating a Sample Dataframe
df = pd.DataFrame({"day": [1,2], "num_passengers": [3,4]})
df['month']= month

# Printing the dataframe
print(df.head())


df.to_parquet(f"output_{month}.parquet")

print('hello pipeline, month', month)