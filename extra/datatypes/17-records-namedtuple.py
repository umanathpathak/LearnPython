from collections import namedtuple

Car = namedtuple("Car" , "color mileage automatic")
car1 = Car("red", 3812.4, True)

print(car1)  # Car(color="red", mileage=3812.4, automatic=True)

# Accessing fields
print(car1.mileage)  # 3812.4

# Fields are immtuable:
car1.mileage = 12  # AttributeError


