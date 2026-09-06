# Create a Pandas DataFrame

import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Aman'],
    'Age': [16, 17, 18],
    'Marks': [85, 92, 76]
}

df = pd.DataFrame(data)

print(df)