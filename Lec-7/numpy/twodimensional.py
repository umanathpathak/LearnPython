import numpy as np
### work with 2 dimensional array
num2 = [[5,8,9],[3,6,8],[4,4,2]]
num2_array = np.array(num2)

print(num2_array)
print(num2_array.size)
print(num2_array.shape)

l1 = [5,8,9,3,6,8,4,4,2,4,6,7,8,9,5]
l1_array = np.array(l1)
print(l1_array.shape)
print(l1_array)

l1_array = l1_array.reshape((5,3))   #changes the shape of the array / the new shape size must match the orional size otherwise error
print(l1_array.shape)            #after storing the reshaped array back to origional, it will show the updated shape
print(l1_array.size)            # check array size
print(l1_array)                 # print array data
print(l1_array[1:4,0:2])       #extracts particular portion of the array, unlike the list slicing where you can only get a member of list.
print(l1_array[0:3,1:2])

print(np.zeros((5,5)))   #creates a 5x5 metric with all zeros
print(np.ones((4,5)))    #creates a 4x5 metric with all ones
print(np.eye(5))         #identity metric of size 5x5, diagonal is 1, rest are 0.
