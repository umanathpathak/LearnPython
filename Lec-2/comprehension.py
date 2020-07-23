#without list comprehension 
l = []
for i in range(0,100):
    l.append(i*2+1)  #creates a list with formula(i*2+1) for each member in the range 0-99
    
l1 = [ i*2+1 for i in range(0,100)]     # Creating list with comprehension
print(l1)

d1 = { d:d*2+1 for d in range(0,100)} #Creating dictionary with comprehension
print(d1)


t1 = ( t*2+1 for t in range(0,100)) # Creating generator with comprehension
print(t1)       #generators can not be directly printed
for tt in t1:
    print(tt)


#creating a list with complex logic
l = []
for i in range(0,100):
    if i%5 == 0:
        l.append(i)
    else:
        l.append(i*2+1)

l1 = [i if i%5==0 else i*2+1 for i in range(0,100)]  # List comprehension with if else
print(l1)


#creating a list with filter
l = []
for i in range(0,100):
    if i%5 ==0 :        #create a list with only number divisble by 5
        l.append(i)
        
l = [i for i in range(0,100) if i%5 == 0]  #list comprehension with filter
print(l)

# NOTE
# While using comprehension, if you have only "if" statement then it need to mention at the end
#and if you have "if else" then need to mention at the start of the statement


#multiple for loops in dictionary comprehension is allowed
dd1 = { str(a*100)+str(b):a+b for a in range(0,100) for b in range(0,70) }
print(dd1)
print(len(dd1))
