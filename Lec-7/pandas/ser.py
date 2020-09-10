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
d = {'a':10,'b':20,'c':30}

#list as series 
print(pd.Series(data=my_list))

#list as series with index
print(pd.Series(data=my_list,index=labels))
print(pd.Series(my_list,labels))    #------> first will treat as data and second will treat as index

#array as series
print(pd.Series(arr))

#array as series with index
print(pd.Series(arr,labels))

#dict as series
print(pd.Series(d))

'''
The key to using a Series is understanding its index. 
Pandas makes use of these index names or numbers 
by allowing for fast look ups of information (works like a hash table or dictionary).

Let's see some examples of how to grab information from a Series. Let us create two sereis, ser1 and ser2:
'''
'''
ser1 = pd.Series([1,2,3,4],["USA","Germany","France","China"])
ser2 = pd.Series([1,2,3,4],["USA","Itly","Germany","England"])

print(ser1 + ser2)
'''

#Multi-Index and Index Hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
#print(hier_index)
#print(hier_index[0])
#print(type(hier_index[0]))
hier_index = pd.MultiIndex.from_tuples(hier_index)
#print(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

#Access data
print(df.loc['G1'])
print(df.loc['G1',1]) # OR
print(df.loc['G1'].loc[1])

#Index names
print(df.index.names)
df.index.names = ['Group','Num']
print(df.index.names)
print(df)