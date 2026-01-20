import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Age": [25, 30, 35, 28, 40, 45, 32, 29],
    "Salary": [50000, 60000, 75000, 52000, 90000, 110000, 67000, 58000]
}

df = pd.DataFrame(data)
print(df)

#adding a column
df["bonus"] = df['Salary'] * 0.1  # 10% bonus
print("after adding bonus column:")
print(df)

#adding a column on desired place == insertion
df.insert(0, "Country", ["USA", "USA", "USA", "USA", "USA", "USA", "USA", "USA"])
print("after inserting Country column at index 0:")
print(df)

#updating values
df.loc[0, 'Age'] = 26  # updating age of first row
print("after updating age of first row:")   
print(df)