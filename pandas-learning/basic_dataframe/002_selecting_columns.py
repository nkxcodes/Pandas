import pandas as pd

df = pd.read_csv("pandas-learning/data/students.csv")

# Q21: Print only the name column.
print(df["name"])

# Q22: Print only the marks column.
print(df["marks"])

# Q23: Print name and marks.
print(df[["name", "marks"]])

# Q24: Print name, age and city.
print(df[["name", "age", "city"]])