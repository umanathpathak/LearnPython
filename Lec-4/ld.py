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

#lambda function to calculate area of circle
calc_circle_area = lambda radius : radius * 3.14
print(calc_circle_area(5))

