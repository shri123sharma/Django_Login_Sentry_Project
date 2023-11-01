# class Dog:
#     attr1 = "mammal"
      
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         return self.name
        
# print(Dog.attr1)
# obj1=Dog("rogger")
# print(obj1.name)
# obj2=Dog("Tommy")
# print(obj2.name)
# obj3=Dog("white")
# print(obj3.speak())
# print(obj2.speak())
# print(obj1.speak())



# class Animal:
#     def __init__(self,name):
#         self.name=name
    
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow!"
    
# obj1=Dog("buddy")
# obj2=Cat("whiskers")

# print(obj1.speak())
# print(obj2.speak())


# class Employee:
#    count = 0       
   
#    def __init__(self,num):
#       for val in num:      
#         self.firstName = val
#         Employee.count += 1
      
# employee1 = Employee([1,2,3,45,56,6])
# employee1 = Employee([10,20,30,40])
# print(employee1.count)


# list1=[2,3,4,5]
# fn=list1[0]
# sn=list1[0]
# for i in list1:
#     if (fn>i):
#         fn=[i]
#     if (sn>i and fn<i):
#         sn=[i]
# print(sn)

# n=[1,2,1,3,2,4]
# c=n[0]
# count=0
# d={}
# for i in n:
#     if (c==i):
#         count+=1
#     d+=dict(i,count)
# print(d)

# class Employee:
    
#     total = 0
    
#     def add_emp(self):
#         self.total +=1
        
# aa = Employee()
# print(aa.total)
# aa.add_emp()
# print(aa.total)
# bb= Employee()
# print(bb.total) #1
# bb.add_emp()
# print(bb.total) #2

# class Employee:
#     total=0
    
#     def __init__(self):
#         self.news =0
    
#     # @classmethod
#     def add(self):
#         self.total+=1
#         self.news +=1
    
        
# obj1=Employee()
# obj1.add()
# print(obj1.news)
# obj2=Employee()
# obj2.add()
# print(obj2.news)
# obj3=Employee()
# obj3.add()
# print(obj3.total)

#inheritance example 
# class Person:
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
        
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
        
#     def detail(self):
#         print(f"my name is {self.name}")
#         print(f"my idnumber is {self.idnumber}")
        
# class Employee(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
        
#         Person.__init__(self,name,idnumber)
        
#     def detail(self):
#         print(f"My name is {self.name}")
#         print(f"Idnumber is {self.idnumber}")
#         print(f"post is {self.post}")
        
    
# obj1=Person("shri",33232)
# print(obj1.name)
# print(obj1.display())
# print(obj1.detail())
# obj2=Employee("rahul",32323,200000,"interns")
# print(obj2.detail())

# # polymorphism
# class Animal():
#     def __init__(self,name):
#         self.name=name
    
#     def make_sound(self):
#         pass
# class Dog():
#     def make_sound(self):
#         return 
# obj1=Animal("shrikant")
# print(obj1.make_sound())

class Animal:
    def __init__(self,name):
        self.name=name
    
    def make_sound(self):
        return f"hello{self.name}"

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says meow!"
    
    
obj1=Dog("buddy")
obj2=Cat("Whisker")

def func(val):
    return val.make_sound()

print(func(obj1))

class Base:
    def __init__(self):
        self.a="geeks"
        self.__c="hello"
        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.__c)
        
obj1=Base()
print(obj1.a)


class Student:
    def __init__(self):
        self.__name="shrikant"
        self.__age=23

    def get_name(self):
        return f"{self.__name} is called"
    
    def set_name(self,name):
        if len(name)>0:
            self.__name=name
            
    def get_age(self):
        return f"{self.__age} is called"
    
    def set_age(self,age):
        if age>0:
            self.__age=age
            
obj1=Student()
print(obj1.get_name())
print(obj1.set_name("arun"))
print(obj1.get_name())


class OldClass:
    def __init__(self,name):
        print(f"i am instance variable{name}")
        
class NewClass:
    def __init__(self):
        print("i am old instance variable")
        
OldClass("hello")
NewClass()


class GetTest:
    def __init__(self):
        print("Greetings")
        
    def get_value(self):
        print("i am another method which is used to more get_value method")
        
obj1=GetTest()
obj1.get_value()

            

