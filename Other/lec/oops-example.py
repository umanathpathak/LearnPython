'''
#1.Encapsulation
#2.Inheritance
#3.Abstraction
#4.Polymorphism

            Person
              |
        -------------
        |           |
    Employee     Employer
       |
    --------
    |      |
Director Manager

'''

class Person():
    pass

class Employee(Person):   #Employee class is child class of Person, Inheritance
    def __init__(self,name='Unknown',salary=0):
        self.name = name
        self.salary = salary
        print("Object of class is created")
        
    def whoAmI(self):
        print("I am " + self.name + " and my Salary is " + str(self.salary))
        
class Employer(Person):
    pass

class Director(Employee):  
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
            
class Manager(Employee):
    name = 'Unknown1'
    salary = 1
    
    def __init__(self,name='Unknown',salary=0,team_size=8):
        Employee.__init__(self,name,salary)
        self.team_size = team_size
    #dunder method
    def __str__(self):
        return "I am " + self.name
    def __repr__(self):
        return "I am " + self.name
    def __len__(self):
        return self.salary
    def whoAmI(self):                 #Parent class whoAmI() method is overriden. This is operator overloading.
        print("I am Manager and my Salary is " + str(salary))

mgr1 = Manager('ALok',20000,15)
mgr1.whoAmI()
mgr1.team_size

dir2 = Director('Yogesh',1000000)
dir2.whoAmI()
dir2.team_size

dir(mgr1)
mgr1.name = 'Alok'
mgr1.role = 'Manager'
mgr1.role
len(mgr1)
print(mgr1)
mgr1


mgr2 = Manager("Hardik",80000)
mgr2.name
mgr2.salary

print(mgr1.name, mgr2.name, Manager.name)

mgr1.__class__.__base__
Manager.__base__

