#A single underscore: Private variable, it should not be accessed directly. But nothing stops you from doing that (except convention).
#A double underscore: Private variable, but not accessible outside class.

class myGun(object):
   def __init__(self):
      self.gunname = "AKM"
      self._bullet = 7.62
      self.__rgstno = 12345

   def getRgstno(self):
      print(self.__rgstno)

   def setRgstno(self,num):
      self.__rgstno = num

obj = myGun()
print(obj.gunname)
print(obj._bullet)
print(obj._myGun__rgstno)
#print(obj.__rgstno)   #------> This will give error as you can not access variable which has double underscore (__)
obj.getRgstno()
obj.setRgstno(67890)
obj.getRgstno()
print(obj._myGun__rgstno)