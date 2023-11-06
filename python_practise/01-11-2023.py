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
        
# def display(self):
#     print(self.name)
#     print(self.idnumber)
    
# def detail(self):
#     print(f"my name is {self.name}")
#     print(f"my idnumber is {self.idnumber}")
        
# class Employee(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
        
#         Person.__init__(self,name,idnumber)
        
#     def detail(self):
#         print(f"My name is {self.name}")
#         print(f"Idnumber is {self.idnumber}")
#         print(f"post is {self.post}")
        
    



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
        

#     def make_sound(self):
#         pass
# class Dog():
#     def make_sound(self):
#         return 
# obj1=Animal("shrikant")
# print(obj1.make_sound())


    
# def make_sound(self):
#     return f"hello{self.name}"

# class Dog(Animal):
#     def make_sound(self):
#         return f"{self.name} says Woof!"
    
# class Cat(Animal):
#     def make_sound(self):
#         return f"{self.name} says meow!"
    
    
# obj1=Dog("buddy")
# obj2=Cat("Whisker")






# class Base:
#     def __init__(self):
#         self.a="geeks"
#         self.__c="hello"
        
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print(self.__c)
        
# obj1=Base()
# print(obj1.a)


# class Student:
#     def __init__(self):
#         self.__name="shrikant"
#         self.__age=23

#     def get_name(self):
#         return f"{self.__name} is called"
    
#     def set_name(self,name):
#         if len(name)>0:
#             self.__name=name
            
#     def get_age(self):
#         return f"{self.__age} is called"
    
#     def set_age(self,age):
#         if age>0:
#             self.__age=age
            
# obj1=Student()
# print(obj1.get_name())
# print(obj1.set_name("arun"))
# print(obj1.get_name())


# class OldClass:
#     def __init__(self,name):
#         print(f"i am instance variable{name}")
        
# class NewClass:
#     def __init__(self):
#         print("i am old instance variable")
        
# OldClass("hello")
# NewClass()


# class GetTest:
#     def __init__(self):
#         print("Greetings")
        
#     def get_value(self):
#         print("i am another method which is used to more get_value method")

    
# printFibb(7)

# def Maximize(a:list, n:int): 
#         value=0
#         s1=sorted(a)
#         print(s1)
#         for i in s1:
#             index=s1.index(i)
#             result=i*index
#             value+=result
#             print(value)
#         # return result

# a = [5, 3, 2, 4, 1]
# a=[1,2,3]
# a=[6,6,8,19,8,10,19,14,20,18,5,11,20,6,10,7,15,8,8,9]
# n=20
# Maximize(a,n)


# def Maximize1(a:list,n:int):
#     value=0
#     s1=sorted(a)
#     for i in range(0,len(s1)): 
#         result=s1[i]*i
#         value+=result
#     return value
# a=[6,6,8,19,8,10,19,14,20,18,5,11,20,6,10,7,15,8,8,9]
# n=20
# print(Maximize1(a,n))

# Input: nums = [3,2,3]
# Output: 3


# ls1=[10,434,434,4,6578,78,3323,5468,79,21213354]

# for i in range(0,len(ls1)):
#     for j in range(i+1,len(ls1)):
#         if ls1[i]>ls1[j]:
#             ls1[i],ls1[j]=ls1[j],ls1[i]
# print(ls1)

# for i in range(0,len(ls1)):
#     val=range(i+1,len(ls1))
#     if ls1[i]>ls1[val]:
#         ls1[i],ls1[val]=ls1[val],ls1[i]
# print(ls1)

# N = 17
# count = 0

# if N <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, N):
#         if N % i == 0:
#             count += 1

# if count >= 1:
#     print("Not a prime number")
# else:
#     print("Prime number")



# def isPrime (N):
#         count=0
#         if N<=1:
#             return 0
            
#         elif N<=2:
#             return 1
            
#         else:
#             for i in range(2,N):
#                 if N%i==0:
#                     count+=1
#         if count>=1:
#             return 0
#         else:  
#             return 1
# N=9
# print(isPrime(N))

# def is_prime1(N):
#     if N<=1:
#         return 0
#     for i in range(2,int(N**0.5)+1):
#         if N%i==0:
#             return 0
#     return 1
# N=9
# print(is_prime1(N))
# print(int(N**0.5)+1)

# def func(A1,N):
#     ls1=[]
#     for i in range(N):
#         if i<len(A1)-1:
#             if A1[i]>A1[i+1]:
#                 ls1.append(arr[i+1])
#             elif A1[i]<A1[i+1]:
#                 ls1.append(-1)
#     ls1.append(-1)
#     return ls1         
# n=5
# arr=[4,2,1,5,3]
# n=6
# arr=[5,6,2,3,1,7]
# print(func(arr,n))

# def func(s,x):
#     if x in s:
#         val=s.find(x)
#         print(val)    
#     else:
#         print(-1)
        
# s="GeeksForGeeks"
# x="For"
# func(s,x)

    
