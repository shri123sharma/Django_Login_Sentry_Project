class Robot():
    pass 
if __name__=='__main__':
    x=Robot()
    y=Robot()
    y2=y
    print(y==y2)
    print("X",id(x))
    print("y",id(y))
    print("y2",id(y2))
    print(x is y)

class Robot():
    pass
x=Robot()
print("x",id(x))
y=Robot()
print("y",id(y))
x.name="marvin"
y.build=1992
print(type(x.name))
x1=x
print("x1",id(x1))
print(x.name)
print(x.__dict__)
print(y.__dict__)

class Robot():
    pass
x=Robot()
print(type(x.__class__))
Robot.brand=1921
print(x.brand)
Robot.brand="Thales"
print(x.brand)
print(Robot.__dict__)
print(x.__dict__)

print(Robot.energy)

def method(obj):
    print("hi"+obj.age)

class Robot():
    pass
x=Robot()
x.name='marvin'
# method(Robot)
y  = Robot()
y.age= "34"
method(y)
print(x.__dict__)
#print(Robot.__dict__)
method(Robot)

class Test():
    
    pass
Test.name="test"
print(Test.__dict__)
x=Test()
x.age="34"
print(x.__dict__)

def hi(obj):
    print("Hi, I am " + obj.name + "!")
class Robot:
    pass
x = Robot()
x.name = "Marvin"
hi(x)

def met(obj):
    print("hi"+obj.name+"!")

class Test():
    say_hi=met
x=Test()
print(type(Test))
print(type(x))
print(x)
x.name="test_user_1"
Test.say_hi(x)

class Person():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"hello,i am {self.name} and i am {self.age}")

print(type(Person))

person_1=Person("shri",23)
print(type(person_1))
print(id(person_1))

person_2=Person("rahul",24)
print(type(person_2))
print(id(person_2))

class A():
    def __init__(self):
        print("intializing class attribute")
x=A()
print(x)

class Robot():
    def __init__(self,name):
        self.name=name
        print(self.name)
x=Robot("Ram")
x.name="marvin"
print(x.__dict__)

class Robot():
    def __init__(self,name=None):
        self.name=name
        print(self.name)

    def say_hi(self):
        if self.name:
            print("hi i am "+self.name)
        else:
            print("Hi, I am a robot without a name")

x=Robot("marvin")
x.say_hi()
y=Robot()
y.say_hi()
print(x.__dict__)

class Robot():
    def __init__(self,name=None):
        self.name=name
        print(self.name)

    def say_hi(self):
        if self.name:
            print("hi am"+"  "+self.name)
        else:
            print("hi i am without a"+self)

    def set_name(self,name):
        self.name=name
        print(self.name)
      
    def get_name(self,name):
        self.name=name
        print(self.name)

x=Robot("marvin")
x.set_name("henry")
x.say_hi()
x.get_name(x.set_name)
y=Robot()

class Robot():
    
    def __init__(self,name,build_year):
        self.name=name
        self.build_year=build_year
        print(f"name  {self.name} and build_year  {self.build_year}")

    def method_1(self):
        if self.name:
            print(f"this is with a name{self.name}")
        else:
            print(f"this is without name for variable")
        if self.build_year:
            print(f"this is with a build_year{self.build_year}")
        else:
            print(f"this  is without build_year for variable")
      
    def set_name(self,name):
        self.name=name
        print(self.name)

    def get_name(self):
        print(self.name)

    def set_build_year(self,build_year):
        self.build_year=build_year
        print(self.build_year)

    def get_build_year(self):
        print(self.build_year)
      
x=Robot("rahul","1998")
x.method_1()
x.set_name("shri")
x.get_name()
x.set_build_year("2121")
x.get_build_year()

class A:
    def __str__(self):
        return "42"
a = A()
print(repr(a))
print(str(a))

class A:
    def __repr__(self):
        return 42
a = A()
print(repr(a))
print(str(a))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
# x=Person('rahul',25)
# print(x.__repr__())

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):    
        return f"Employee {self.name} ({self.age})"
    
    def __repr__(self):
        return self.name
person = Person1("RAM",23)

print(person.__repr__)
print(person.__str__)

class Robot():
    def __init__(self,name,build_year):
        self.name=name
        self.build_year=build_year

    def __repr__(self):
        return "Robot"+self.name+str(self.build_year)
    
    def __str__(self):
        return "Robot"+self.name+str(self.build_year)
    
if __name__=="__main__":
    x=Robot("marvin",2012)
    x_str=str(x)
    print(x_str)

    print(type(x_str))

class Myclass():
    def __init__(self,name,age,email):
        self.name=name #public attribute
        self._age=age  #protected attribute
        self.__email=email #private attribute

    def do_something(self):
        self.name+=1  #public method
        self._age+=1  #protected method
        self.__email+=1 #private method
        print(self.name.__dict__())

obj=Myclass(1,2,3)
print(obj.name)
print(obj._age)
print(obj._Myclass__email)
print(obj.do_something)

import datetime
now=datetime.datetime.now()
print(now)
print("using str",now.__str__())
print("using repr",now.__repr__())

class Robot():
    class_att="i am a class atrribute"
x=Robot()
print(x.class_att)
y=Robot()
print(y.class_att)
print(x.__dict__)
print(Robot.__dict__)

class Robot():
    
    three_law=(
        """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
"""A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
"""A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
    )

    def __init__(self,name,build_year):
        self.name=name
        self.build_year=build_year

x=Robot("user_1",23)
print(type(x.three_law))

class C:
    counter=0
    def __init__(self):
        self.counter+=1

    def __del__(self):
        self.counter-=1

if __name__=="__main__":
    x=C()
    print("number of instance")

class MyClass:
    some_class_variable = "foo"

    @staticmethod
    def my_static_method(arg1, arg2):
        print(arg1)
        print(arg2)
        print(MyClass.some_class_variable)
MyClass.my_static_method("rahul", 24)
x=MyClass()
x.my_static_method("rahul",24)

class Robot:
    __counter=0
    print(type(__counter))

    @staticmethod
    def my_static_method(arg1,arg2):
        pass

class Myclass():
    def __init__(self,value):
        self.value=value
        
    def get_value(self):
        return self.value
x=Myclass(10)
print(x.get_value())

class My_class():
    
    def __init__(self,value):
        self.value=value

    @staticmethod
    def get_value(x,y):
        return x+y  
My_class(10)
x=My_class(100)
print(x.get_value(100,100))

from datetime import  date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"hello{self.name}{self.age}")

    @classmethod
    def fromBirthday(cls,name,year):
        return cls(name,date.today().year - year)
    
# obj=Person("mayank",23)/
obj_1=Person("rahul",1997)
obj_1.fromBirthday('shri',1996)

class MyClass():
    
    def instance_method(self,name,age):
        self.name=name
        self.age=age
        if self.name=="rahul" and self.age=="23":
            print("this is rahul name and age")

        else:
            print("other user")

    @classmethod
    def class_method(cls,name,age):
        return cls(name,age)
# obj=MyClass()
# obj.instance_method("shri",'23')
obj_1=MyClass()
obj_1.class_method("shri",'23')

class MyClass():
    
    def __init__(self):
        self._x=None
        print(self._x)

    def set_value(self,value):
        self._x=value
        print(self._x)
    
    def get_value(self):
        return self._x
     
obj=MyClass()
obj.set_value(100)
print(obj.get_value())