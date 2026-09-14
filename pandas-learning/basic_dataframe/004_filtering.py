import pandas as pd

df = pd.read_csv('pandas-learning/data/students.csv')

# Q61: Find the students whose marks are greater than 80.
print()
print(df[df['marks'] > 80]) 