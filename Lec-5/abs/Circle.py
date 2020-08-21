from Shape import Shape
class Circle(Shape):
    
  def calc_area(self,radius):
    print("You are going to calculate area of Circle.....")
    return 3.14*radius

carea = Circle()
carea.welcome()   
print(carea.calc_area(5))