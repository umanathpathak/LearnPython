#arguments and key arguments:

# *args (single *) is for position arguments and takes any num of positional arguments.
#no positional argument can follow *args.
#only keyword arguments can follow *args.
def myprint(a,b,c,*arg):
    print(arg)

myprint('sfasd','2343',7868,'asfsdfasdf','asdfasd')

#1st three arguments are mapped to a,b,c and all other positional arguments are read by *arg
#when you print arg, it is a tuple.

def myprint(a,b,c,d=9,*rum):
    print(rum)

myprint('sfasd','2343',7868,'asfsdfasdf','asdfasd')

#positional arguments are mapped based on positions. 
#If no positional arguments specified then you can treat it as keyword arguments. 

#below function takes 3 arguments, a,b,c. 
#it seems a is positional and b & c are keyword arguments. But that is not true.

def abc(a,b=5,c=7):
    print(a,b,c)


abc(7,6)    #7 is mapped to a and 6 is mapped to b.
abc(b=6,a=5) #a takes 5, b takes 6 (overrrides 5), c takes default value 7.
abc(c=9,a=3) #a takes 3, b takes default 5, c takes 9 (overrides 7).
abc(b=8,c=6) #ERROR!! No value is passes to a.


#**keyargs is for passing multiple keyword arguments to a function.
#No positional or keyword argument can follow **keyarg.
#Everything else should be written before **keyarg.
def mysum(**keyargs):
    keyargs['c']=9
    print(keyargs)

mysum(a=2,b=9,c=7,d=5,e=6,r=4)

#keyargs returns a dictionary.
