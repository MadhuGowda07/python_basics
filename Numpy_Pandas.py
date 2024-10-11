import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)        #NumPy Array: [1 2 3 4 5]


#Array of Zeros and Ones
zeros_arr = np.zeros((3, 3))
print("Array of Zeros:\n", zeros_arr)

ones_arr = np.ones((2, 4))
print("\nArray of Ones:\n", ones_arr)
#output
'''
Array of Zeros:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

Array of Ones:
 [[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''


#Array with a Range of Numbers
range_arr = np.arange(0, 11)
print("Array with Range:\n", range_arr)
"""
Array with Range:
 [ 0  1  2  3  4  5  6  7  8  9 10]
"""


#Basic Mathematical Operations
arr = np.array([1, 2, 3, 4, 5])

print("Add 5:", arr + 5)

print("Multiply by 2:", arr * 2)

print("Square:", arr ** 2)

print("Square Root:", np.sqrt(arr))
'''
Add 5: [ 6  7  8  9 10]
Multiply by 2: [ 2  4  6  8 10]
Square: [ 1  4  9 16 25]
Square Root: [1.         1.41421356 1.73205081 2.         2.23606798]
1
​
'''


#Simple Pandas DataFrame
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

print("DataFrame:\n", df)
#output
'''
DataFrame:
       Name  Age         City
0    Alice   24     New York
1      Bob   27  Los Angeles
2  Charlie   22      Chicago
'''


#Read Data from a CSV File
df = pd.read_csv('your_file.csv')
print(df.head())


#Select Specific Columns

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

print("Names:\n", df['Name'])

print("\nNames and Cities:\n", df[['Name', 'City']])
#output
'''
Names:
 0      Alice
1        Bob
2    Charlie
Name: Name, dtype: object

Names and Cities:
       Name         City
0    Alice     New York
1      Bob  Los Angeles
2  Charlie      Chicago
'''


#Basic Statistics
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'Salary': [50000, 60000, 45000]}
df = pd.DataFrame(data)

print("Mean Age:", df['Age'].mean())
print("Maximum Salary:", df['Salary'].max())
#output
'''
Mean Age: 24.333333333333332
Maximum Salary: 60000
'''
