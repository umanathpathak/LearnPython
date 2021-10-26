from types import MappingProxyType


writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)

print(read_only["one"])
print(read_only.items())

# read_only["three"] = 5 # raises TypeError
