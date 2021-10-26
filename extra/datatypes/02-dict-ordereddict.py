import collections

arranged_dict = collections.OrderedDict(one=1, two=2, three=3)

print(arranged_dict["one"])

arranged_dict["four"] = 4

print(arranged_dict.items())

unarranged = {"first": 1, "second": 2, "third": 3}
arranged_dict2 = collections.OrderedDict(unarranged)

print(arranged_dict2)
