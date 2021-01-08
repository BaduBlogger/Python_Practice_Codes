import pandas as pd

s1 = pd.Series([1,2,3,4,5,6,7])
print(s1)

print(s1+5)	#i.e. 0th location + 5 so the output starts from the element 6 till 12

s2 = pd.Series([11,22,33,44,55,66,77])	
#s2 = pd.Series([11,22,33,44,55,66])	#output comes in float and last element is displayed as Nan

print(s2)

print(s1+s2)	#output gives int and addition of two arrays

print(s1-s2)	#output gives int and Subtraction of two arrays