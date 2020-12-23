import numpy as np

n1 = np.array([[1,2,3],[4,5,6]])

print(n1)	#displaying the Array elements

print("Shape of the Array is :")	#printing the shape i.e. dimensions of Array

print(n1.shape)

print("Changing the shape of array :")

n1.shape = (3,2)

print(n1.shape)

print("The array after :")

print(n1)

