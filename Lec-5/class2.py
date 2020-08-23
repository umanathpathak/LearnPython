
'''
starting variable from single underscore (_) is a private variable but can be accessible.

starting variable from double underscore (__) is treated as private unaccessible variable. This is used for abstraction and encapsulation.

__init__ ---> All classes have a function called __init__(), which is always executed when the class is being initiated.

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''

class Bike:
    
    def __init__(self, name, wheel, colour, gear, minspeed, maxspeed):
        self.name = name
        self.wheel = wheel
        self.colour = colour
        self.gear = gear
        self.minspeed = minspeed
        self.maxspeed = maxspeed

    def nature(self):
        if self.maxspeed > 130:
            print("My bike is sport bike")
            #self.avg = "between 20 to 30"
            #self._avg = "between 20 to 30"
            #self.__avg = "between 20 to 30"
        else:
            print("My bike is not a sport bike")
            #self.avg = "between 30 to 40"
            #self._avg = "between 30 to 40"
            #self.__avg = "between 30 to 40"
    
    def milage(self):
        print("My bike gives milage {}".format(self.avg))
        #print("My bike gives milage {}".format(self._avg))
        #print("My bike gives milage {}".format(self.__avg))

x = Bike("tvs", 2,"Blue",6,0,120)
x.nature()
x.milage()
print(x.avg)
#print(x._avg)
#print(x.__avg)
