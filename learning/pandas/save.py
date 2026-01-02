import pandas as pd

data = {
    "name" : ["Alice", "Bob", "Charlie"],
    "age" : [25, 30, 35],
    "city" : ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

df. to_csv("save_output.csv")  # save dataframe to csv file and create a file named save_output.csv