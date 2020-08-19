class CalcArea():

  def __init__(self, *args):
    self.args = args()

  def calc_area(self,r):
    area = 3.14 * r * r
    print("Area of circle is {}".format(area))

  def calc_area(self,l,w):
    area = l * w
    print("Area of rectangle is {}".format(area))