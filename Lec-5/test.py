import sys

#print(len(sys.argv))
if len(sys.argv) == 1:
    print("You need to pass either one number or two number with space in both number.")
elif len(sys.argv) == 2:
    print(sys.argv[1])
elif len(sys.argv) == 3:
    print(sys.argv[1:3])
else:
    print("You are passing more parameter")

