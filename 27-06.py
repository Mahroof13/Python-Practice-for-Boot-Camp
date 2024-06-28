import pandas as pd

# Example 1: Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series from a list:")
print(series)

# Example 2: Creating a Series with a custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=index)
print("\nPandas Series with custom index:")
print(series_with_index)

# Example 3: Creating a Series from a dictionary
data = {'x': 100, 'y': 200, 'z': 300}
series_from_dict = pd.Series(data)
print("\nPandas Series from a dictionary:")
print(series_from_dict)

# Example 4: Accessing elements in a Series
print("\nAccessing elements in a Series:")
print("Element at index 'y':", series_from_dict['y'])
print("First element:", series[0])

# Example 5: Performing operations on a Series
print("\nPerforming operations on a Series:")
print("Series + 5:")
print(series + 5)
print("Series > 25:")
print(series > 25)
