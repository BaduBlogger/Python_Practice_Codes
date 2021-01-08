import pandas as pd

s1 = pd.Series({'a':100,'b':200,'c':300})	# Created a Dictionary Type structure
s2 = pd.Series([1,2,3,4,5,6,7],index=['a','b','c','d','e','f','g'])	#Assigning Index i.e. Key Values for the list
s3 = pd.Series({'a':100,'b':200,'c':300},index=['a','is','yummy','c','b'])	#Changing Index Position i.e. Rearranging and the key which are not there has value NaN

print(s1)
print(s2)
print(s3)