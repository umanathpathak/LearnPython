import numpy as np

#work with single dimensional array
num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array)
#for i in range(len(num_array)):
#    print(num_array[i])

#diff between list and array
#print(num + 10)
print(num_array + 10)

rnum = np.arange(1,5,2)
print(rnum)

print(np.random.randint(1,6,5))  #generates 5 random integers between 1 and 6 inclusive
print(np.random.random(6))       #generates 6 random numbers between 0 and 1
print(np.linspace(1,10,101))     #divides 1 and 10 into 101 euqal parts
print(np.min(num_array))          #return minimum from l2_array
print(np.argmin(num_array))       #return the index of the minimum from num_array
print(np.max(num_array))          #return maximum from l2_arra
print(np.argmax(num_array))       #return the index of the maximum from num_array

