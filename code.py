import pandas as pd
import csv

df = pd.read_csv("merged_data.csv")
print(df.shape)

print(list(df))

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

print("After Deleting", df.shape)
print(list(df))

df.to_csv("newdata.csv")