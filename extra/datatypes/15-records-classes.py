class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

    # def __repr__(self):
    #     return f"{self.__class__.__name__}(color={self.color}, mileage={self.mileage}, automatic={self.automatic})"


car1 = Car("red", 3812.4, True)
car2 = Car("blue", 40231.0, False)

# Get the mileage:
car2.mileage # 40231.0

# Classes are mutable:
car2.mileage = 12
car2.windshield = "broken"

# String representation is not very useful
# (must add a manually written __repr__ method):
print(car1) # <Car object at 0x1081e69e8>