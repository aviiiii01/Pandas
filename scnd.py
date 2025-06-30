import pandas as pd

#SERIES
#  a series is like a column in a table it is simply a one dimensional array holding data of any type..
 
#it is like a 1-D array but the major differnce is that in array there is a static index which is in number 0,1,2,3,4,5,..
# but in Series we can labell the index in the way we want just like a map(infact map has also limit that it can map a particular type of data!!!...)
#  we can also access an items using the labelor custom index that we have made.


a=[1,2,3]
x=pd.Series(a)# by default indexing(label) will be 0,1,2,3,4,5,...
print(x)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    6

y=pd.Series(a,index=["x","y",1])
print(y)
# x    1
# y    2
# 1    3

aa={"hui":[1,2,34],"bui":2,"cui":3}
z=pd.Series(aa)
print(z)
# hui    1
# bui    2
# cui    3
print("###################")
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])# from this we can only make a series of items with label day1 and day2 

print(myvar)


