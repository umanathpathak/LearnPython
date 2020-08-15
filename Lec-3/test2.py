
#Learning variable scope
#LEGB = Local, Enclosing, Gloabl, Build-in

## examples for GLOBAL variables #########
n1=4
n2=5
l1 = [1,2]
def add2(num1,num2,l1):  
    #global n1     #Now this value is referring to the n1 outside the function
    n1=70           #this will chagne the global n1
    print(n2)
    l1[0] = 50
    return num1+num2

add2(n1,n2,l1)
print(n1)           #Now you can not get n1=4 value as its memory ref number changed due to global n1 defined in function  

'''
n1=4
n2=5
l1 = [1,2]
def maths():
    global n2
    n2=10
    def add2(num1,num2,l1):  
        global n1     #Now this value is accessible outside the function
        n1=70
        l1[0] = 50
        print( num1+num2 )
    add2(n1,n2,l1)
maths()

#### examples for NONLOCAL / ENCLOUSER variables ############
n1=4
n2=5
l1 = [1,2]
def maths():
    n2=10
    def add2(num1,num2,l1):  
        nonlocal n2         #To access enclouser value, not local and not global
        n2=30
        n1=70
        print("withing add2 function n2 is {}".format(n2))
        l1[0] = 50
        print( "ans is : {}".format(num1+num2) )
    add2(n1,n2,l1)
    print("Within maths func n2 is {}".format(n2))
maths()
print("Outside all n2 is {}".format(n2))   



'''