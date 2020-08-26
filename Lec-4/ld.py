'''
Lambda is one type function which accept parameter and do proces which is mentioned inside lambda function and provide output.

syntax
lambda arguments : expression
'''

x = lambda a : a + 10
print(x(5))

#Above code is equivalent to below code

def tenadd(num):
    return num + 10

print(tenadd(5))

#create a simple function to return the first letter of string in lower case.
def first_letter(str1):
    return str1[0].lower()
    
#Change the above function into Lambda expression 
f = lambda str1 : str1[0].lower().lower()

#Lets test it
first_letter('Asfsd')
f('Assfsd')
 
#create another lambda expression to join first letters of two strings
f = lambda str1,str2 : str1[0].lower()+str2[0].upper()
f('Assfsd','wqrer')


#lambda expresssion example
g = lambda str1:(str1[0].lower() if str1[1] == 'A' else str1[0].upper())
g('asddf')
g('dAasd')

g = lambda str1:(str1[0].lower() if str1[1] == 'A' else None)

g('asddf')
g('dAasd')


#lambda function to calculate area of circle
calc_circle_area = lambda radius : radius * 3.14
print(calc_circle_area(5))