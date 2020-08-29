'''
DataFrames are the workhorse of pandas and are directly inspired by the R programming language. 
We can think of a DataFrame as a bunch of Series objects put together to share the same index. 

Let's use pandas to explore this topic!
'''
import numpy as np 
import pandas as pd

df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
#print(df)
'''
#Select single column
print(df['W'])

#Check data type
print(type(df['W']))

#SQL syntax but not recommonded
print(df.W)

#Select multiple column by passing list
print(df[['W','Z']])

#Creating a new column
df['Total'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)

#Remove column
print(df.drop('Total',axis=1))
print(df)
print(df.drop('Total',axis=1,inplace=True))
print(df)

#Remove row
print(df.drop('E',axis=0))
print(df)
print(df.drop('E',axis=0,inplace=True))
print(df)

#Select Row by loc function
print(df.loc['A'])

#Select Row by iloc function
print(df.iloc[2])

#Select data with combination of row and column
print(df.loc['A','W'])
print(df.loc[['A','B'],['W','Z']])

'''

'''
#Conditional select
print(df>0)
#print(df[df>0])

#print(df[['W','Y']])
#print(df)
#print(df[df['W']>0])
#print(df[df['W']>0]['Y'])
#print(df[df['W']>0][['Y','Z']])

#if Multiple condition use ()
print(df[(df['W']>0) & (df['Y']>0)])

'''
'''
#play with index
#we can reset index 
print(df)
df.reset_index()
print(df)
df.reset_index(inplace=True)
print(df)


#declare column as new index
print(df)
newind = 'MH KL TL HP DL'.split()
df['States'] = newind
print(df)
df.set_index('States')
print(df)
df.set_index('States',inplace=True)
print(df)
'''