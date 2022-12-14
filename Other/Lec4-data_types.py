# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:51:17 2018

@author: nilesh_indore
"""

'''List - Array of any type, defined by [ ], no need to declare length,
it is mutable, can be defined by list() also.
'''
import copy

mydetails = ['Nilesh', 35, 7738003350, 'AIPL']

print(mydetails)
print(mydetails[0])
print(mydetails[1])
print(mydetails[2])
print(mydetails[3])

range_test = list(range(mydetails[1]))
print(range_test)

print(mydetails[0:2])
print(mydetails[:2])

# add new member in list
mydetails.append("Kalwa")
print(mydetails)
print(mydetails[4])
# delete particular member from list
mydetails.remove("Kalwa")
print(mydetails)
print(mydetails[4])
mydetails.append("Nerul")
print(mydetails)

print(mydetails[0::3])

print(len(mydetails))
print(len(range_test))

# addition of list
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
range_test = list(range(mydetails[1]))
print(mydetails + range_test)

# operation on list
print(mydetails * 3)

print([mydetails] * 3)

# for loop with list
for i in mydetails:
    print(i)

# extend list vs append list
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
anotherlist = ['ext1', 'ext2', 'ext3']
mydetails.extend(anotherlist)
print(mydetails)
print(anotherlist)
anotherlist.extend(mydetails)
print(anotherlist)
anotherlist.append(mydetails)
print(anotherlist)

# Insert in list
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
mydetails.insert(1, 'M')

# index of list
print(mydetails.index("Nilesh"))
print(mydetails.index("M", 2))  # will search after index5

# sorting of list
list_test_sort = ['xyz', 'pqr', 'abc']
range_rest_soft = [4, 8, 3, 1]
list_test_sort.sort()
range_rest_soft.sort()
list_test_sort.reverse()
range_rest_soft.reverse()

# reverse the list
list_test_sort[::-1]
print(list_test_sort)

# pop with list
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
age = mydetails.pop(1)  ## will remove it from list and assigning to new variable, need to provide index value
print(mydetails)

# remove with list
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
mydetails.remove("Nilesh")  ## need to provide actual value from list

# creat list with comprehensions
list1 = [i ** 2 for i in range(5)]
print(list1)

''' above thing is short form of below code
list1 = []
for i in range(5):
    list1.append(i**2)
print(list1)
'''

list2 = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(5)]
print(list2)

# map with list
ord('a')
list(map(ord, 'a'))
list(map(ord, 'spam'))
# use of map support you have function which write power of that number
# map(myfuction,listofnumers)

print(sorted('Nilesh'))

# Dictionary - defined by {}, use key:value pair
dic1 = {'name': 'Nilesh', 'age': 35}
print(dic1)
print(dic1['name'])
print(dic1['age'])

dic2 = {[('name', 'Mayura'), ('age', 30)]}
print(dic2)
print(dic2['name'])
print(dic2['age'])

dic1.fromkeys(["location"])

print(dic1.items())
print(dic1.keys())
print(dic1.values())

# Tuples - immutable, ordered collection, defined by () but can be defined without it also.
# can be defined by tuple function also.
t = ('Nanabhau', 'Vatsala', 'Arnav', 'Arnav')
print(t)
t.index('Arnav')
t.count('Arnav')

# Sets - immutable but can be append, fixed length, unordered collection, repetation not allowed
test_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
set1 = set(test_list)
set2 = set([6, 7, 8, 9, 6, 7, 8])
set2.add(30)
print(set1)
print(set2)

# Magic
mydetails = ['Nilesh', 35, 7738003350, 'AIPL']
mydetails1 = ['Nilesh', 35, 7738003350, 'AIPL']
mydetails2 = mydetails
print(mydetails)
print(mydetails1)
print(mydetails2)
mydetails2[1] = 40
print(mydetails)
print(mydetails1)
print(mydetails2)
del mydetails2[1]
print(mydetails)
print(mydetails1)
print(mydetails2)

mydetails is mydetails1
mydetails == mydetails1

mydetails is mydetails2
mydetails == mydetails2

id(mydetails)
id(mydetails1)
id(mydetails2)

# if you make changes in mydetails2 will affect mydetails to avoid that copy will help
mydetails = ['Nilesh', 35, 7738003350, 'AIPL', [1, 2]]
mydetails1 = ['Nilesh', 35, 7738003350, 'AIPL', [1, 2]]
mydetails2 = mydetails
mydetails3 = mydetails.copy()
mydetails3[1] = 100
print(mydetails)
print(mydetails1)
print(mydetails2)
print(mydetails3)
mydetails3[4][1] = 10
mydetails4 = copy.deepcopy(mydetails)
print(mydetails4)
mydetails4[4][1] = 100
print(mydetails4)
print(mydetails)
print(mydetails1)
print(mydetails2)
print(mydetails3)