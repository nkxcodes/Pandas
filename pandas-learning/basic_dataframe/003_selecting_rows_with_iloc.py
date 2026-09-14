import pandas as pd

df = pd.read_csv("pandas-learning/data/students.csv")

# iloc stands for integer location.
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

# Q40: Select rows 5-10
print()
print(df.iloc[5:11].to_string(index=False))

# Q41: Select the first 3 rows and first 3 columns.
print()
print(df.iloc[0:3, 0:3])

# Q42: Select the first 5 rows and only the name and marks columns using iloc.
print()
print(df.iloc[0:5, [1, 5]].to_string(index=False))

# Q43: Select the third row and fourth column.
print()
print(df.iloc[2, 3])

# Q44: Select every second row.
print()
print(df.iloc[::2]) # Start:End:Step

# Q45: Select the last 5 rows using iloc.
print()
print(df.iloc[-1:-6:-1])

# Q46: Reverse the order of the rows using iloc.
print()
print(df.iloc[::-1])

# Q47: Select rows 2-7
print()
print(df.iloc[1:7])

# Q48: Select rows 2-7 and columns 1-4:
print()
print(df.iloc[1:7, 0:4])

# Q49: Select only the first column.
print()
print(df.iloc[:, 0]) # [:, 0] - Series, [:, [0]] - DataFrame

# Q50: Select only the last column.
print()
print(df.iloc[:, -1])

# Q51: Set id as the index.
print()
df = df.set_index('id')
print(df)

# Q52: Select the student with id 5.
print()
print(df.loc[5])

# Q53: Select students with IDs 3 through 7.
print()
print(df.loc[3:7])

# Q54: Select name for a particular ID.
print()
print(df.loc[3, 'name'])

# Q55: Select name and marks for a particular ID.
print()
print(df.loc[4, ['name', 'marks']])

# Q56: Select all students whose id is greater than 5.
print()
print(df.loc[df.index > 5])

# Q57: Reset the index.
df = df.reset_index()

# Q58: Set name as the index.
df = df.set_index('name')