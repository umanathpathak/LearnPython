arr = bytes((0, 1, 2, 3))
print(arr)

print(arr[0])
print(id(arr[0]))
print(id(arr[1]))
print(id(arr[2]))
print(id(arr[3]))

arr1 = b'\x00\x01\x02\x03'
print(arr1)

arr2 = bytes(range(0, 255))
print(arr2)


# arr2[1] = 2
# del arr2[1]
