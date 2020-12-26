import numpy as np

n1 = np.array([10,20,30,40,50])
np.save('my_array',n1)		#for saving array, first parameter:"Userdefined name", second parameter:"array object"

n2 = np.load('my_array.npy')	#for loading the array into new object, .npy for numpy array
print(n2)