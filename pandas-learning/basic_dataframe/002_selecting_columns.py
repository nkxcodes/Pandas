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

# Q25: Store the marks column in a variable
marks = df["marks"]

# Q26: Check the type of that variable.
print(type(marks))

# Q27: Store name and marks in another DataFrame.
student_df = df[["name", "marks"]]

# Q28: Print the first 5 rows of name and marks.
print(df[["name", "marks"]].head())

# Q29: Print all columns except gender.
print(df.drop(columns=["gender"]))

# Q30: Print all columns except age
print(df.drop(columns="age"))