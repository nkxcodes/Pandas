import pandas as pd

df = pd.read_csv("pandas-learning/data/students.csv")

# Q36: Select the first row using iloc.
print()
print(df.iloc[0])

# Q37: Select the second row.
print()
print(df.iloc[1])

# Q38: Select the last row.
print()
print(df.iloc[-1])