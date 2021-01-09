import pandas as pd

iris = pd.read_csv('iris.csv')

print(iris.min())

print(iris.max())

print(iris.mean())

print(iris.median())

#Pandas Function

print(iris.head())

def double_make(s):
	return s*2
	
print(iris[['Sepal.Width','Petal.Width']].apply(double_make))

print(iris['Species'].value_counts())

print(iris.sort_values(by='Sepal.Length'))