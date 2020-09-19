#Decorators allow you to make simple modifications to callable objects like functions, methods, or classes.

def repeater(fun):
    def r2(*args,**kwds):
        fun(*args,**kwds)
        fun(*args,**kwds)
    return r2

@repeater
def add2(num1, num2):
    print(num1 + num2)

add2(2,3)