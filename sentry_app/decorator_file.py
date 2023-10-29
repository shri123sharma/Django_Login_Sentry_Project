from call_decorator_file import *

# def func(name="shrikant"):
#     return "hi"+" "+name
# print(func())
# print(id(func))

# greet=func
# print(greet)

# # del func
# # print(func())

# print(greet())
# print(id(greet))

# def func2(hello,name="rahul"):
#     print(hello+" "+name)
#     def func_a():
#         return "now you are in the func_a() function"
    
#     def func_b():
#         return "now you are in the func_a() function"
    
#     print(func_a())
#     print(func_b())
#     print("again back func2")
# print(func2("hi"))


# def func3(name="hello"):
#     print("function 3 call")
#     def func4(name="shrikant"):
#         print('func 4 return value')
#         return func5()
#     def func5():
#         print('func 5 return value')
#         return "this is fuc5 call"
#     return func4()
# print(func3())

# def hi(name="sharma"):
#     def greet1():
#         return "now in this function is greet1 function"
    
#     def greet2():
#         return "now in this function is greet2 function"
    
#     if name=="sharma":
#         return greet1
#     else:
#         return greet2
    
# a=hi()
# print(a())

# def hi():
#     return "hi shrikant"

# def my_function(func):
#     print(func)
#     print("this is my_function call")
#     print(func())

# my_function(hi)

# @my_decorator
# def say_hello(name):
#     print(f"Hello,{name}")
# say_hello("Alice")

# @my_add_decorator
# def add(a,b):
#     return a+b
# result=add(10,30)
# print(result)

# @my_cap_decorator
# def func():
#     return "helloworld"
# result1=func()
# print(result1)


# def outer_function(x):
#     def inner_function(y):
#         return x+y
#     return inner_function
# closure_instance=outer_function(10)
# print(id(closure_instance))
# result=closure_instance(5)
# print(id(result))
# print(result)


# def hi(name="shrikant"):
#     def greet():
#         return "now you are in the greet() function"
    
#     def welcome():
#         return "now you are in the welocome()function"
    
#     if name=="shrikant":
#         return greet

#     else:
#         return welcome

# a=hi()
# print(id(a))
# print(a())

def add_question(question):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(question)
            result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator

@add_question("what is your name?")
def greet(name):
    print(f"Hello,{name}")
greet("Alice")


def upper_decorator(func):
    print(f"this is func object{func}")
    def wrapper(self,text):
        result=func(self,text.upper())
        return result
    return wrapper

class TextManpulation:
    def __init__(self):
        pass
    @upper_decorator
    def process_text(self,text):
        return text
    
instance_obj1=TextManpulation()
result=instance_obj1.process_text("hello,world")
print(result)