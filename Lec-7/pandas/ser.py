'''
The first main data type we will learn about for pandas is the Series data type. 
Let's import Pandas and explore the Series object.

A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). 
What differentiates the NumPy array from a Series, is that a Series can have axis labels, 
meaning it can be indexed by a label, instead of just a number location. 
It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.
'''
import numpy as np
import pandas as pd

#You can convert a list,numpy array, or dictionary to a Series: 
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
oarr = np.array([10,20,30,40])
marr = oarr.reshape(2,2)
d = {'a':10,'b':20,'c':30}

#list as series 
#print(pd.Series(data=my_list))

#list as series with index
#print(pd.Series(data=my_list,index=labels))
#print(pd.Series(my_list,labels))    #------> first will treat as data and second will treat as index

#array as series
#print(pd.Series(oarr))
#print(pd.Series(marr))     #-----> it will give error, series work with only 1 dimesnsional

#array as series with index
#print(pd.Series(arr,labels))

#dict as series
#print(pd.Series(d))