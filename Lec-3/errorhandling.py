import sys
try:
    num = int(input("Enter any number : "))    
except:
    print("Invalid number")
    sys.exit()
print(num)