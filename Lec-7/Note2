#Lets see Exception handling. Something not acceptable is encountered by python which is error, python throws exceptions.
#To handle exceptions, we should use try/except/finally. finally is optional.

#Code with probable rrrors should be kept within try block.
#In case of any error except block will be executed.
#Irrespective of any error, finally block will always be executed.

#note that errors occuring in the except or finally block are still be unhandled.

num1 = 10
num2 = 0
try:
    ans = num1/num2
    print(ans)
except ZeroDivisionError:
    print("Division by 0 is not possible")
except TypeError:
    print("Both should be numeric.")
except:
    print("Some error has happened")
finally:
    print("I will always come")  
    
    
#To rasie user defined exceptions,you need to define a class with excetion name.

class IDoError(Exception):
  pass
  
num1 = 10
num2 = 0
try:
    if num1 == 10:
        raise IDoError
    ans = num1/num2
    print(ans)
except IDoError:
    print("I have made some error")
except ZeroDivisionError:
    print("Division by 0 is not possible")
except TypeError:
    print("Both should be numeric.")
except:
    print("Some error has happened")
finally:
    print("I will always come")  
