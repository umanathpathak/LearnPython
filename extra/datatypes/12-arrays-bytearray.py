arr = bytearray((0, 1, 2, 3))
print(arr)

print(arr[0])
print(id(arr[0]))
print(id(arr[1]))
print(id(arr[2]))
print(id(arr[3]))
print(id(arr[4]))

arr1 = bytearray(range(0, 255))
print(arr1)


arr1[1] = 2
del arr1[1]

bytes_arr = bytes(arr)
print(bytes_arr)