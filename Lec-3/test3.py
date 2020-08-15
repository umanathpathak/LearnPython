import sys

print("This program is to calculate area of shape. Select shape to calculate area. \n")

try:
    option=int(input("Enter 1=circle, 2=rectangle, 3=square : "))
    if option > 3 or option <= 0:
        print("Invalid option") 
        sys.exit()
except:
    print("Invalid option")
    sys.exit()

print("Hello")

if option == 1:
    radius = int(input("Enter raidus size : "))
elif option == 2:
    ln = int(input("Enter lenght of rectangle : "))
    wd = int(input("Enter width of rectangle : "))
elif option == 3:
    side = int(input("Enter size of one side square : "))

def circle_area(r):
    carea=3.14*r*r
    print(carea)

def rect_area(l,w):
    rarea=l*w
    print(rarea)

def square_area(s):
    sarea=s*s
    print(sarea)