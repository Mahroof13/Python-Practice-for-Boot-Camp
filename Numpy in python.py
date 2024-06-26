import numpy as np

# Initial array and its properties
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array: \n{arr}")
print(f"Shape of array: {arr.shape}")
print(f"Data type of array elements: {arr.dtype}")
print(f"Total number of elements: {arr.size}")
print()

# Creating arrays using different methods
arr1 = np.array([1, 2, 3])
print(f"Array created with np.array(): {arr1}")
print()

arr2 = np.zeros((2, 3))
print(f"Array created with np.zeros():\n{arr2}")
print()

arr3 = np.ones((3, 2), dtype=int)
print(f"Array created with np.ones():\n{arr3}")
print()

arr4 = np.arange(0, 10, 2)
print(f"Array created with np.arange(): {arr4}")
print()

arr5 = np.linspace(0, 1, 5)
print(f"Array created with np.linspace(): {arr5}")
print()

arr6 = np.random.rand(2, 3)
print(f"Array created with np.random.rand():\n{arr6}")
print()

# Element-wise operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Element-wise addition:\n{arr1 + arr2}\n")
print(f"Element-wise multiplication:\n{arr1 * arr2}\n")

# Aggregation functions
arr = np.array([[1, 2], [3, 4]])
print(f"Sum of all elements: {np.sum(arr)}")
print(f"Column-wise minimum: {np.min(arr, axis=0)}")
print(f"Row-wise maximum: {np.max(arr, axis=1)}\n")

# Matrix operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Matrix multiplication:\n{np.dot(arr1, arr2)}\n")
print(f"Transpose of a matrix:\n{arr1.T}\n")

# Broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
result = arr1 * scalar
print(f"Array multiplied by scalar:\n{result}\n")

arr1 = np.array([[1, 2], [3, 4]])  
arr2 = np.array([10, 20])          
result = arr1 + arr2
print(f"Broadcasting result:\n{result}\n")

# Indexing and slicing
arr = np.array([1, 2, 3, 4])
print(f"First element: {arr[0]}")
print(f"Second element: {arr[1]}")
print(f"Sum of third and fourth elements: {arr[2] + arr[3]}\n")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f"2nd element on 1st row: {arr[0, 1]}")
print(f"5th element on 2nd row: {arr[1, 4]}\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(f"Elements from index 1 to 4: {arr[1:5]}")
print(f"Elements from index 4 to end: {arr[4:]}")
print(f"Elements up to index 4: {arr[:4]}")
print(f"Elements from index -3 to -1: {arr[-3:-1]}")
print(f"Elements from index 1 to 5 with step 2: {arr[1:5:2]}")
print(f"Elements with step 2: {arr[::2]}\n")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"Elements from row 1 and columns 1 to 3: {arr[1, 1:4]}")
print(f"Elements from rows 0 to 1 and column 2: {arr[0:2, 2]}")
print(f"Elements from rows 0 to 1 and columns 1 to 3: {arr[0:2, 1:4]}\n")

# Data types
arr = np.array([1, 2, 3, 4])
print(f"Data type of array elements: {arr.dtype}\n")

arr = np.array(['apple', 'banana', 'cherry'])
print(f"Data type of array elements: {arr.dtype}\n")

arr = np.array([1, 2, 3, 4], dtype='S')
print(f"Array with string type elements: {arr}")
print(f"Data type of array elements: {arr.dtype}\n")

arr = np.array([1, 2, 3, 4], dtype='i4')
print(f"Array with integer type elements: {arr}")
print(f"Data type of array elements: {arr.dtype}\n")

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(f"Array with float to integer conversion: {newarr}")
print(f"Data type of new array elements: {newarr.dtype}\n")

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(f"Array with integer to boolean conversion: {newarr}")
print(f"Data type of new array elements: {newarr.dtype}\n")

# Reshaping and concatenation
arr = np.arange(1, 10)
print(f"Original array: {arr}")
arr_reshaped = arr.reshape(3, 3)
print(f"Reshaped array:\n{arr_reshaped}\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
arr_concatenated = np.concatenate((arr1, arr2), axis=0)
print(f"Concatenated array along axis 0:\n{arr_concatenated}\n")

# Splitting and modifying arrays
arr = np.arange(1, 10)
print(f"Original array: {arr}")
arr_split = np.split(arr, 3)
print("\nSplit arrays:")
for part in arr_split:
    print(part)

arr = np.array([1, 2, 3, 4, 5])
arr_appended = np.append(arr, [6, 7])
print(f"\nAppended array: {arr_appended}")

arr_deleted = np.delete(arr, [1, 3])
print(f"Array after deletion: {arr_deleted}\n")
