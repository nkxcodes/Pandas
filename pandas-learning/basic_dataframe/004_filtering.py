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

# Q66: Find students from Mumbai.
print()
print(df[df['city'] == 'Mumbai'])

# Q67: Find students whose gender is Male.
print()
print(df[df['gender'] == 'Male'])

# Q68: Find female students.
print()
print(df[df['gender'] == 'Female'])

# Q69: Find students with marks greater than and equal to 75.
print()
print(df[df['marks'] >= 75])

# Q70: Find students with marks greater than and equal to 40.
print()
print(df[df['marks'] <= 40])

# Q71: Find students between 60 and 80 marks.
print()
print(df[(df['marks'] >= 60) & (df['marks'] <= 80)])

# Q72: Find students older than 17.
print()
print(df[df['age'] > 17])

# Q73: Find students younger than 18.
print()
print(df[df['age'] < 18])

# Q74: Find students from Delhi with marks greater than 80.
print()
print(df[(df['city'] == 'Delhi') & (df['marks'] > 80)])