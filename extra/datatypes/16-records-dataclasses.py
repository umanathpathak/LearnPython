from dataclasses import dataclass

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


car1 = Car("red", 3812.4, True)

# Instances have a nice repr:
print(car1)  # Car(color='red', mileage=3812.4, automatic=True)

# Accessing fields:
print(car1.mileage)  # 3812.4

# Fields are mutable:
car1.mileage = 12
car1.windshield = "broken"

# Type annotations are not enforced without
# a separate type checking tool like mypy:
print(Car("red", "NOT_A_FLOAT", 99))  # Car(color='red', mileage='NOT_A_FLOAT', automatic=99)