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

# Q39: Select rows 0-4.
print()
print(df.iloc[0:5].to_string(index=False)) # .to_string(index=False) is used to not give index in the output