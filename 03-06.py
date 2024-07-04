import pandas as pd

# Original DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
})

# Detecting null values
print("Detecting null values in the entire DataFrame:")
print(df.isnull(), "\n")

print("Detecting null values in column 'A':")
print(df['A'].isnull(), "\n")

# Detecting non-null values
print("Detecting non-null values in the entire DataFrame:")
print(df.notnull(), "\n")

print("Detecting non-null values in column 'A':")
print(df['A'].notnull(), "\n")

# Dropping null values
print("Dropping rows with any null values:")
print(df.dropna(), "\n")

print("Dropping columns with any null values:")
print(df.dropna(axis=1), "\n")

print("Dropping rows where all values are null:")
print(df.dropna(how='all'), "\n")

# Filling null values
print("Filling null values with 0:")
print(df.fillna(0), "\n")

print("Filling null values with column mean:")
print(df.fillna(df.mean()), "\n")

print("Filling null values forward (ffill):")
print(df.fillna(method='ffill'), "\n")

print("Filling null values backward (bfill):")
print(df.fillna(method='bfill'), "\n")

# Replacing null values
print("Replacing null values with 0:")
print(df.replace(to_replace=None, value=0), "\n")

print("Replacing null values in column 'A' with 100:")
df['A'] = df['A'].replace(to_replace=None, value=100)
print(df, "\n")

print("Replacing null values with 'Unknown':")
print(df.replace(to_replace=None, value='Unknown'), "\n")

# Interpolating missing values
print("Interpolating missing values using linear method:")
print(df.interpolate(), "\n")

print("Interpolating missing values using quadratic method:")
print(df.interpolate(method='quadratic'), "\n")

print("Interpolating missing values using polynomial method (order 2):")
print(df.interpolate(method='polynomial', order=2), "\n")

# Checking for any null values
print("Checking if any null values exist in the DataFrame:")
print(df.isnull().values.any(), "\n")

print("Checking if any null values exist in column 'A':")
print(df['A'].isnull().values.any(), "\n")

# Summarizing null values
print("Count of null values in each column:")
print(df.isnull().sum(), "\n")

print("Count of null values in column 'A':")
print(df['A'].isnull().sum(), "\n")

print("Total count of null values in the DataFrame:")
print(df.isnull().sum().sum(), "\n")

# New Example DataFrame
new_df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', None, 'Linda'],
    'Age': [28, 24, None, 35, 32],
    'Salary': [None, 54000, 58000, 61000, None]
})

# Detecting null values
print("Detecting null values in the new DataFrame:")
print(new_df.isnull(), "\n")

print("Detecting null values in column 'Age':")
print(new_df['Age'].isnull(), "\n")

# Dropping null values
print("Dropping rows with any null values in the new DataFrame:")
print(new_df.dropna(), "\n")

print("Dropping columns with any null values in the new DataFrame:")
print(new_df.dropna(axis=1), "\n")

print("Dropping rows where all values are null in the new DataFrame:")
print(new_df.dropna(how='all'), "\n")

# Filling null values
print("Filling null values with 0 in the new DataFrame:")
print(new_df.fillna(0), "\n")

print("Filling null values with column mean in the new DataFrame:")
print(new_df.fillna(new_df.mean()), "\n")

print("Filling null values forward (ffill) in the new DataFrame:")
print(new_df.fillna(method='ffill'), "\n")

print("Filling null values backward (bfill) in the new DataFrame:")
print(new_df.fillna(method='bfill'), "\n")

# Replacing null values
print("Replacing null values with 0 in the new DataFrame:")
print(new_df.replace(to_replace=None, value=0), "\n")

print("Replacing null values in column 'Name' with 'Unknown' in the new DataFrame:")
new_df['Name'] = new_df['Name'].replace(to_replace=None, value='Unknown')
print(new_df, "\n")

# Interpolating missing values
print("Interpolating missing values using linear method in the new DataFrame:")
print(new_df.interpolate(), "\n")

print("Interpolating missing values using quadratic method in the new DataFrame:")
print(new_df.interpolate(method='quadratic'), "\n")

print("Interpolating missing values using polynomial method (order 2) in the new DataFrame:")
print(new_df.interpolate(method='polynomial', order=2), "\n")

# Checking for any null values
print("Checking if any null values exist in the new DataFrame:")
print(new_df.isnull().values.any(), "\n")

print("Checking if any null values exist in column 'Age' in the new DataFrame:")
print(new_df['Age'].isnull().values.any(), "\n")

# Summarizing null values
print("Count of null values in each column in the new DataFrame:")
print(new_df.isnull().sum(), "\n")

print("Count of null values in column 'Age' in the new DataFrame:")
print(new_df['Age'].isnull().sum(), "\n")

print("Total count of null values in the new DataFrame:")
print(new_df.isnull().sum().sum(), "\n")
