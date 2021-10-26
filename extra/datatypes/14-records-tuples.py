# Fields: color, mileage, automatic
car1 = ("red", 3812.4, True)
car2 = ("blue", 40231.0, False)

# Tuple instances have a nice repr:
print(car1) # ('red', 3812.4, True)
print(car2) # ('blue', 40231.0, False)

# Get mileage:
print(car2[1]) # 40231.0

# Tuples are immutable:
car2[1] = 12  # error

# No protection against missing or extra fields
# or a wrong order:
car3 = (3431.5, "green", True, "silver")

