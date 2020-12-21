import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")
# print the dataset
print(df)
# print number of features and their types
print(df.head())
print(df.dtypes)

df_clean = df.drop_duplicates(keep='first')
print(df_clean)

df_clean.dropna(inplace = True)

print(df_clean.isnull().sum())
