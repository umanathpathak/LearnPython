'''
def addition(n1,n2):
    return(n1+n2)

def substract(n1,n2):
    return(n1-n2)

def multiplication(n1,n2):
    return(n1*n2)

def division(n1,n2):
    return(n1/n2)

print(addition(20,10))
print(multiplication(20,10))
print(substract(20,10))
print(division(20,10))
###################################################
# Function inside function

def math(n1,n2):
    num1=n1
    num2=n2
    def addition(n1,n2):
        return(n1+n2)
    
    def substract(n1,n2):
        return(n1-n2)
    
    def multiplication(n1,n2):
        return(n1*n2)
    
    def division(n1,n2):
        return(n1/n2)

    print(addition(num1,num2))
    print(substract(num1,num2))
    print(multiplication(num1,num2))
    print(division(num1,num2))

math(20,10)

###################################################

'''
#write function to calculate area for circle, rectangle and square with error handling