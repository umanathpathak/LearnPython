car1 = {
    "color": "red",
    "mileage": 3812.4,
    "automatic": True,
}

car2 = {
    "color": "blue",
    "mileage": 40231,
    "automatic": False,
}

# Dicts have a nice repr:
print(car2)  # {'color': 'blue', 'automatic': False, 'mileage': 40231}

# Get mileage:
print(car2["mileage"])  # 40231

# Dicts are mutable:
car2["mileage"] = 12
car2["windshield"] = "broken"
print(car2)




# advantages over dicts:

car_dict = {
    "color": "red",
    "mileage": 3812.4,
    "automatic": True,
}
# make sure the names of the attributes are consistent.
# For instance {'colour': 'blue', 'mileage': 3000.0, 'automatic': False} will not work as expected.

car_tuple = ('red', 3812.4, True) # need to remember the order of the attributes






# No protection against wrong field names,
# or missing/extra fields:
car3 = {
    "colr": "green",
    "automatic": False,
    "windshield": "broken",
}
