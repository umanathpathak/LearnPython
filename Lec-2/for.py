# When we need to repeat any task for number of time, we use for loop

#for i in range(5):
#    print(i)

student_names=['nilesh','mayura','arnav']
student_marks=[56,78,93]
student_marksheet={'nilesh':39,'mayura':52,'arnav':74}
for i in student_names:
    print("Student name : ", i)

#for (a,b) in zip(student_names,student_marks):
#    print(a , " : " , b)

#Sort even odd number
even_num = [ ]
odd_num = [ ]
for num in range(0,100):
    if num%2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print(even_num)
print(odd_num)


# continue....break in for loop
for h in range(10):
    if h==3:
        continue        #skips the next statements and shifts pointer to the top of the loop
    print(h,h**2)
    if h==7:
        break           #break the loop abruptly and changes the pointer to the end of the loop
else:
    print("I am out of for loop")   #executes when for loop has ended without executing break