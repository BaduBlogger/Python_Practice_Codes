import numpy as np

n1 = np.array([11,12,13,14])
n2 = np.array([21,22,23,24])

print('Original Arrays are :')
print(n1)
print('\n')
print(n2)

print('After vertically stacking both Arrays we get:') 		#joining two array one below the other
print(np.vstack((n1,n2)))

print('After horizontally stacking both Arrays we get:')	#joining two array one after other
print(np.hstack((n1,n2)))

print('After column stacking both Arrays we get:')		#joining them in column form like array1 = column1 and array2 = column2
print(np.column_stack((n1,n2)))