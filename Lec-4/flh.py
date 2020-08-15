'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

import os

if not os.path.exists("test.txt"):
    data = open("test.txt","x")

data = open("test.txt","rt")
#print(data.read())
#print(data.readline())
#print(data.readlines())

for i in data:
    print(i)

data.close()

data = open("test.txt","at")
data.write("One thing is left to say bye.")
data.close()

data = open("test.txt","rt")
print(data.read())
data.close()

data = open("test.txt","wt")
data.write("One thing is left to say bye.")
data.close()

data = open("test.txt","rt")
print(data.read())
data.close()

#if os.path.exists("test.txt"):
#    os.remove("test.txt")
