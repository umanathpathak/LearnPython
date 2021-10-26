import collections


jersey_numbers = collections.defaultdict(int)
jersey_numbers["ms dhoni"] = 7
jersey_numbers["virat kohli"] = 18
print(jersey_numbers["x player"])

print(jersey_numbers)


######
# team = collections.defaultdict(list)
#
# team["india"].append("Virat Kohli")
# team["india"].append("Jaspreet Bumrah")
# team["england"].append("Josh Butler")
#
# print(team)

####


###
#
# kwargs = {'a': 10, 'b': 12, 'c': 13}
# d_int = collections.defaultdict(int, **kwargs)
# print(d_int['d'])
