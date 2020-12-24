import numpy as np

n1 = np.array([10,20])
n2 = np.array([100,200])

print('Sum of Array is :')	#simple sum of array elements (two different arrays)
print(np.sum([n1,n2]))

print('Sum of Array for Axis - 0 :')	#Adds values column wise i.e. vertically of two different Arrays
print(np.sum([n1,n2],axis=0))

print('Sum of Array for Axis - 1 :')	#Adds values row wise i.e. horizontally of two different Arrays
print(np.sum([n1,n2],axis=1))

