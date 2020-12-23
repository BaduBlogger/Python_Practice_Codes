import numpy as np

n1 = np.zeros((1))	#creating 1D array.

print(n1)

n2 = np.zeros((5,5))	#creating 5X5 array with 5 rows and 5 columns with default data type float

print(f'2D Array : \n{n2}')	#here f and {} is used for formatting purpose and \n for new line

n3 = np.zeros((2,4),dtype=int)	#creating 2X4 array with 2 row and 4 columns with datatype int

print('2D Array :'+'\n'+str(n3))	#here str() is used to convert the result in string and + is used to concat