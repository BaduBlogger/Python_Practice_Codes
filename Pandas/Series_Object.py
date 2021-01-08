import pandas as pd
import numpy as np

list1 = [1,2,3,4,5,6]	#list of 6 elements
s1 = pd.Series(list1)	#Here the series object if filled with list elements as per their index from 0 and data type is also printed
s2 = pd.Series([1,2,3])	#Second Method Directly passing list

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])	#By creating Array
s3 = pd.Series(arr1)

print(s1)
print(s2)
print(s3)