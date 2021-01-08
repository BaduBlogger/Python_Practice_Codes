import pandas as pd

s1 = pd.Series([1,2,3,4,5,6,7,8,9])

print(s1)

print(s1[7])	#Here element at index 7 is displayed

print(s1[:6])	#Here 0-5 are display and 6 is excluded

print(s1[-3:])	#Here last 3 elements are displayed

print(s1[-5:])