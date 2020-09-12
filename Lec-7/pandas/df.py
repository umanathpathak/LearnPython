'''
DataFrames are the workhorse of pandas and are directly inspired by the R programming language. 
We can think of a DataFrame as a bunch of Series objects put together to share the same index. 

Let's use pandas to explore this topic!
'''
import numpy as np 
import pandas as pd

df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

#Select single column
#print(df['W'])

#Check data type
#print(type(df['W']))

#SQL syntax but not recommonded
#print(df.W)

#Select multiple column by passing list
#print(df[['W','Z']])

#Creating a new column
#df['Total'] = df['W'] + df['X'] + df['Y'] + df['Z']
#print(df)

#Remove column
#print(df.drop('Total',axis=1))
#print(df)
#print(df.drop('Total',axis=1,inplace=True)) #----> to reflect change in actual data need to use inplace parameter
#print(df)

#Remove row
#print(df.drop('E',axis=0))
#print(df)
#print(df.drop('E',axis=0,inplace=True))
#print(df)

#Select Row by loc function
#print(df.loc['A'])

#Select Row by iloc function
#print(df.iloc[2])

#Select data with combination of row and column
#print(df.loc['A','W'])
#print(df.loc[['A','B'],['W','Z']])

#Conditional select
#print(df>0)
#print(df[df>0])

#print(df[['W','Y']])
#print(df)
#print(df[df['W']>0])
#print(df[df['W']>0]['Y'])
#print(df[df['W']>0][['Y','Z']])

#if Multiple condition use ()
#print(df[(df['W']>0) & (df['Y']>0)])

#play with index
#we can reset index 
#print(df)
#df.reset_index()
#print(df)
#df.reset_index(inplace=True)
#print(df)

#declare column as new index
#print(df)
#newind = 'MH KL TL HP DL'.split()
#df['States'] = newind
#print(df)
#df.set_index('States')
#print(df)
#df.set_index('States',inplace=True)
#print(df)

# access csv file as dataframe
#csvdf = pd.read_csv(r'C:\Nilesh Indore\Projects\LearnPython\Lec-7\pandas\student.csv')
#print(csvdf.head())
#print(csvdf.columns)
#print(type(csvdf))

# access xlsx file as dataframe
#xlsxdf = pd.read_excel(r'C:\Nilesh Indore\Projects\LearnPython\Lec-7\pandas\student.xlsx')
#print(xlsxdf.head())
#print(xlsxdf.columns)
#print(type(xlsxdf))

'''
The key to using a Series is understanding its index. 
Pandas makes use of these index names or numbers 
by allowing for fast look ups of information (works like a hash table or dictionary).

Let's see some examples of how to grab information from a Series. Let us create two sereis, ser1 and ser2:
'''

ser1 = pd.Series([1,2,3,4],["USA","Germany","France","China"])
ser2 = pd.Series([1,2,3,4],["USA","Itly","Germany","England"])
print(ser1)
print(ser2)
#print(ser1 + ser2)


#Multi-Index and Index Hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
#print(hier_index)
#print(hier_index[0])
#print(type(hier_index[0]))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

#Access data
#print(df.loc['G1'])
#print(df.loc['G1',1]) # OR
#print(df.loc['G1'].loc[1])
#print(df.loc['G1',1]['B'])
#print(df.loc['G1'].loc[1]['B'])

#Index names
#print(df.index.names)
#df.index.names = ['Group','Num']
#print(df.index.names)
#print(df)