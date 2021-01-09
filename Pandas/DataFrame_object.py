import pandas as pd

df = pd.DataFrame({'Name':['Sam','Mukta','Mumma','Matt'],'Marks':[99,32,100,78]})

print(df)	#Printing Dataframe

#DataFrame Built-in Functions

iris = pd.read_csv('iris.csv')

print(iris.head())	#Displaying Top 5 Values

print(iris.tail())	#Displaying tail 5 Values

print(iris.shape)	#Displaying Rows and column

print(iris.describe())	#Displays Mean max min std_dev 75% etc

#Accessing data from DataFrame

print(iris.head())

print(iris.iloc[0:5,0:3])	#gives 0:5 rows and 0:3 columns and iloc for index of locations 

print(iris.loc[5:11,('Sepal.Length')])	#gives 5:11 rows and column name is to be specified

print(iris.head())

print(iris.drop('Sepal.Length',axis=1))	#COlume name and axis = 1 is colume

print(iris.drop([3,4,5,6],axis=0))	# deletes rows with index 3,4,5,6 and axis = 0 is rows
