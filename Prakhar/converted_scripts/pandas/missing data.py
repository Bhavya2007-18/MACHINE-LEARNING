import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Age": [25, None, 35, 28, 40, 45, 32, 29],
    "Salary": [50000, None, 75000, 52000, 90000, 110000, 67000, 58000]
}

df = pd.DataFrame(data)
print(df)

print("\nChecking for missing data:")
print(df.isnull())  # check for missing data  TRUE = MISSING DATA
print("\nCount of missing data in each column:")
print(df.isnull().sum())  # count of missing data in each column

# Handling missing data

# 1. Drop rows with missing data
#df.dropna(axis=0, inplace=True)  # drop rows with missing data , if axis=1 then drop columns with missing data
#print("\nData after dropping rows with missing data:")
#print(df)


# 2. Fill missing data with a specific value (e.g., mean of the column)
df.fillna(df.mean(numeric_only=True), inplace=True)
# fill missing data with mean of the column
print("\nData after filling missing data with mean:")
print(df)                                                     # only one thing can work here at a time either dropna or fillna

# interpolation == filling of estimated values
data2 = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Age": [25, None, 35, 28, None, 45, 32, 29],
    "Salary": [50000, None, 75000, 52000, 90000, None, 67000, 58000]
}
print("before interpolation:")
df2 = pd.DataFrame(data2)
print(df2)

df['Age'] = df2['Age'].interpolate()  # interpolate missing values in Age column
print("\nAfter interpolation of Age column:")
print(df)
      
