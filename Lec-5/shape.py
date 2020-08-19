from abc import ABC

class Shape(ABC):
  def welcome(self):
    print("This program is about calculating area of different shapes.")

  def calc_area(self):
    print("You are going to calculate area of Circle.....")
    pass
   

class Circle(Shape):

  def calc_area(self,radius):
    return 3.14*radius

carea = Circle()
carea.welcome()   
print(carea.calc_area(5))

