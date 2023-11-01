class Person:
    # construter method  with initilize attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #  class method    
    def introduce(self):
        print(f"my name is {self.name} and my age is {self.age}")
        
obj1=Person('Alice',23)
obj2=Person('Bob',26)
obj1.introduce()
print(obj1.__dir__())
print(obj2.__dir__())


class Cal(object):
    # class variable
    pi=3.142
    def __init__(self,radius):
        # instance variable
        self.radius=radius
        
    def area(self):
        return self.pi*(self.radius**2)
    
obj1=Cal(32)
print(obj1.pi)
print(isinstance(obj1,Cal))
print(isinstance(obj2,Cal))

class Superclass():
    superpower=[]
    def __init__(self,name):
        self.name=name
        
    def add_superpower(self,power):
        self.superpower.append(power)
        
foo=Superclass('foo')
bar=Superclass('bar')
print(foo.name)
print(bar.name)


class OldClass():
    def __init__(self):
        print('i am old class')
        
class NewClass():
    def __init__(self):
        print('i am new class')
old=OldClass()
new=NewClass()

class GetTest(object):
    def __init__(self):
        print("Greetings")
    
    def another_method(self):
        print("this is another method which is not automatically called")
    
a=GetTest()

# a.another_method()
# obj1.another_method()

class GetTest1(object):
    def __init__(self,name):
       print('Greetings!! {0}'.format(name))
        
    def another_method(self):
        print("another method which is automatically called")
        
obj1=GetTest1("shri")
obj2=GetTest1('sharma')
        