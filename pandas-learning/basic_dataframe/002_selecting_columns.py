import pandas as pd

df = pd.read_csv("pandas-learning/data/students.csv")

# Print only the name column.
print(df["name"])

# Print only the marks column.
print(df["marks"])

# Print name and marks.
print(df[["name", "marks"]])