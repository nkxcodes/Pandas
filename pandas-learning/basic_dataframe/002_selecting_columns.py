import pandas as pd

df = pd.read_csv("pandas-learning/data/students.csv")

# Q21: Print only the name column.
print()
print(df["name"])

# Q22: Print only the marks column.
print()
print(df["marks"])

# Q23: Print name and marks.
print()
print(df[["name", "marks"]])

# Q24: Print name, age and city.
print()
print(df[["name", "age", "city"]])

# Q25: Store the marks column in a variable
print()
marks = df["marks"]

# Q26: Check the type of that variable.
print()
print(type(marks))

# Q27: Store name and marks in another DataFrame.
print()
student_df = df[["name", "marks"]]

# Q28: Print the first 5 rows of name and marks.
print()
print(df[["name", "marks"]].head())

# Q29: Print all columns except gender.
print()
print(df.drop(columns=["gender"]))

# Q30: Print all columns except age
print()
print(df.drop(columns="age"))

# Q31: Create a DataFrame containing only name, city and marks.
print()
df_2 = df[["name", "city", "marks"]]

# Q32: Find the number of unique cities.
print()
print(df["city"].nunique())