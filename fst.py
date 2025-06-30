import pandas as pd

#creating dataFrame
#A DataFrame in the pandas library for Python is primarily used -
# to represent and work with tabular, two-dimensional, labeled data structures

#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns
data={
    'cars':["BMW","Volvo","Mercedes"],
    'seats':[2,4,4]
}#in the form of a dictionary!!!....

#there will be indexing also in dataFrame as 0,1,2,3,4,5 in rows
dataset=pd.DataFrame(data) #making a dataset in the form of rows and columns where each pair of the dict act as a column name and values at each row ..

print(dataset)
print(pd.__version__)

