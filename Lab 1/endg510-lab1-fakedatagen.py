import pandas as pd # in case of error, install pnadas using: pip install pandas
# Read the CSV file into a DataFrame
import numpy as np

df = pd.read_csv('data.csv')

def new_data():
    new_data = {
    'Temp': np.random.uniform(low = 200, high = 300),
    'Humd': np.random.uniform(low = 300, high = 1000),
    'Label': 0
    }
    return new_data

i = 0
while i < 50:
    df = df._append(new_data(), ignore_index=True)
    i = i+1

# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data.csv", index=False)