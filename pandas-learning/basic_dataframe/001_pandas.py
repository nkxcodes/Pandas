# Q1: Import pandas
import pandas as pd

# Q2: Read students.csv into a DataFrame
df = pd.read_csv("pandas-learning/data/students.csv")

# Q3: Print the entire DataFrame
print(df)

# Q4: Print the first five rows
print(df.head())

# Q5: Print the first 10 rows.
print(df.head(10))

# Q6: Print the last 5 rows.
print(df.tail())