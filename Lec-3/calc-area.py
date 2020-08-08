import sys

def calc_circle_area(r):
    print("Area of circle is {}".format(3.14*r*r))

def calc_square_area(a):
    print("Area of square is {}".format(a*a))  

def calc_rectangle_area(l,w):
    print("Area of rectangle is {}".format(l*w))

print("This program will help you to calculate area of shapes.")
opt=input("Press 1 for Circle, press 2 for Square, press 3 for Rectangle and press Q for exit : ")

if opt == "Q" or opt == "q":
    sys.exit()

try:
    int(opt)
except:
    print("Invaid option")
    sys.exit()

if int(opt) == 1:
    try:
        num=int(input("Enter radius size : "))
    except:
        print("Invalid value")
        sys.exit()
    calc_circle_area(num)
elif int(opt) == 2:
    try:
        num=int(input("Enter size of one side of square : "))
    except:
        print("Invalid value")
        sys.exit()
    calc_square_area(num)
elif int(opt) == 3:
    try:
        num1=int(input("Enter size of length : "))
    except:
        print("Invalid value")
        sys.exit()
    try:
        num2=int(input("Enter size of width : "))
    except:
        print("Invalid value")
        sys.exit()
    calc_rectangle_area(num1,num2)
else:
    print("This is invalid option.")
    sys.exit()
