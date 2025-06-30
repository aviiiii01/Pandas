import pandas as pd
#LOC

# stands for locate rows
    #Pandas use the loc attribute to return one or more specified row(s)
data={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df=pd.DataFrame(data)
print(df.loc[0])
# calories    420
# duration     50

print(df.loc[[0,1]])# also we can print the multiple rows using list of indeces...

#   calories  duration
# 0       420        50
# 1       380        40

#Named Index:

dff=pd.DataFrame(data,index=["day1","day2","day3"])
print(dff)
#       calories  duration
# day1       420        50
# day2       380        40
# day3       390        45

print(dff.loc["day3"])
# calories    390
# duration     45


#Reading and loading files as a datasets from .csv file 

sett=pd.read_csv('indian_universities.csv')
print(sett)

