'''
__name__ is a special variable which value is "__main__" if that program run itself. 
But if that program get called by some other program then it's value would be filename of that program.
'''

print("This is animal.py")

if __name__ == "__main__":
    print("Calling function by own. __name__ = {}".format(__name__))
else:
    print("Calling function by other program. __name__ = {}".format(__name__))