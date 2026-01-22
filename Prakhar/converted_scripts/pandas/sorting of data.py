import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Age": [25, 30, 35, 28, 40, 45, 32, 29],
    "Salary": [50000, 60000, 75000, 52000, 90000, 110000, 67000, 58000]
}
df = pd.DataFrame(data)
print(df)

#sorting age by ascending order
df.sort_values(by='Age', inplace=True)  # sort by Age column in ascending order
print("\nData sorted by Age in ascending order:")
print(df)
