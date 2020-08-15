'''
Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Syntax
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''

class Bike:

    wheel = 2
    colour = "white"
    gear = 4
    minspeed = 0
    maxspeed = 80

x = Bike()              # Instance/Object creation of class
print(x.wheel)          #Calling attribute of class
print(x.colour)
print(x.gear)
print(x.minspeed)
print(x.maxspeed)

x.wheel = 3
x.colour = "Blue"
x.gear = 6
x.maxspeed = 150
print(x.wheel)          
print(x.colour)
print(x.gear)
print(x.minspeed)
print(x.maxspeed)