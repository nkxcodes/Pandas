import pandas as pd

df = pd.read_csv('pandas-learning/data/students.csv')

# Q61: Find the students whose marks are greater than 80.
print()
print(df[df['marks'] > 80])

# Q62: Find students whose marks are less than 50.
print()
print(df[df['marks'] < 50])

# Q63: Find the students whose marks are exactly 90.
print()
print(df[df['marks'] == 90])

# Q64: Find students whose age is 18.
print()
print(df[df['age'] == 18])

# Q65: Find students from Delhi.
print()
print(df[df['city'] == 'Delhi'])