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