import pandas as pd

df = pd.read_csv('pandas-learning/data/students.csv')

# Q91: Create a passed column where marks >= 33 means True.
print()
df['passed'] = df['marks'] >= 33
print(df[df['passed']])

# Q92: Create failed column.
print()
df['failed'] = df['marks'] < 33
print(df[df['failed']])

# Q93: Create a bonus_marks column containing 5 for everyone.
print()
df['bonus_marks'] = 5
print(df)

# Q94: Create final_marks = marks + bonus_marks
print()
df['final_marks'] = df['marks'] + df['bonus_marks']
print(df)