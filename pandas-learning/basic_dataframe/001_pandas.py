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

# Q7: Print the last 10 rows.
print(df.tail(10))

# Q8: Print the number of rows.
print(len(df)) #or
print(df.shape[0])

# Q9: Print the number of columns.
print(df.shape[1])

# Q10: Find both rowa and columns using shape.
print(df.shape)