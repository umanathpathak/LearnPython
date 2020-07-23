#make sure that you have proper control of the while loop.
#must specify a termination condition, otherwise it will end up in an infinite loop.

#while 2>1:
#    print("haaa")

while 2>1:
    i=input("Enter any alphabet \n")
    if i=='c':
        continue
    elif i=='q':
        break
    print("you have typed",i)
else:
    print("While loop exited without break.")   #Never going to execute