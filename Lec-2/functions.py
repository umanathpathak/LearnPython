#range() is to return a series of numbers
#format - range(start_pos, end_pos, step_size)
print(list(range(5)))           #just 1 argument means it is end_pos, by default start_pos is 0
print(list(range(100,200)))     #returns a series from 100 to 199
print(list(range(100,200,10)))  #step_size skips numbers in between
print(list(range(-10,-2)))      #negative numbers are also allowed in range
print(list(range(-1,-20,-1)))   #negative step_size, does the reverse tranversal

#zip()  Like zip it combines 2 datasource.
#zip function creates tuples from the inputs
a = [1,2,3]
b = [4,5,6]
for (a,b) in zip(a,b):
    print("a * b = ", a * b)

#input()    get input from user
#by default data get from input function is treated as string data type.
name=input("Enter your name \n")
print("Hello " + name )