import numpy as np

n1 = np.array([10,20,30,40,50,60,70])
n2 = np.array([50,60,70,80,90])

print('Intersection of two sets :')
print(np.intersect1d(n1,n2))	#return intersection i.e. common elements from two arrays

print('n1-n2 operation :')
print(np.setdiff1d(n1,n2))	#returns elements which are present in n1 only (excluding common elements) n1-n2 operation

print('n2-n1 operation :')
print(np.setdiff1d(n2,n1))	#return n2-n1