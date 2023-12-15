
def succ(x):
  return x+1
sucesser=succ
print(sucesser(100))

def succ_1(x,y):
  return x+y+100
sucesser_1=succ_1(100,200)

def succ_2():
  return sucesser_1
print(succ_2())

def greet(name):
    return "hello"+".."+name
my_func=greet

print(my_func("BOB"))

def greet_func(func,name):
    return my_func("mdklemdemd")
print(greet_func(my_func,"bob"))

def outer_func():
  print("outer_func")
  def inner_func():
    print("inner_func")
    def deep_inner_func():  
      print("deep_inner_func")
    deep_inner_func()
  inner_func()
outer_func()

def temperature(t):
    print(t)
    print("outer_func_call")
    def celsius2fahrenheit(x):
    
        return 9 * x / 5 + 32

    result =str(celsius2fahrenheit(t)) 
    return result

print(temperature(20))

def second_func():
   
   print("second_func_call")

def first_func(func):
   
   print(func)
   print("first_func_call")
   print("first_func_second_statement")
   func()

first_func(second_func)

def add(a,b):
   print(a+b)

def substract(a,b):
   print(a-b)

def combine(a,b,func_1,func_2):
   print("comnine function call")
   func_1(a,b)
   func_2(a,b)

combine(5,3,add,substract)

def func_1(a,b):
    def func_2(a,b):
        print(a+b)
    return func_2(a,b)
func_1(10,20)

def greeting(lang):
    print(lang)
    print("greeting_func_call")
    def customized_lang(lang):
      print(lang)
      print("customized_func_call")
      if lang=="de":
        phrase="Guten Morgen"
      elif lang=="fr":
        phrase="Bonjour"
      elif lang=="it":
         phrase="Buongionrno"
      elif lang=="tr":
         phrase="Günaydın"
      elif lang=="gr":
         phrase="Καλημερα"
      else:
         phrase="Hi"

      return phrase+lang+"!!!!!" 

    return customized_lang 
say_hi=greeting('tr')
print(say_hi("Gülay"))

def my_decorator(func):

    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

def say_hello():

    print("hello!")

say_hello=my_decorator(say_hello)
say_hello()

def func_1():
    def func_2():
        print("func_2 is call")
    return func_2
func_1()

def f(x):
    print("f func is call")
    def g(y):
        print("g func is call")
        return y+x+3
    return g
f(10)

def greeting_func_gen(lang):
    print('greeting function is call')
    def customized_greeting(name):
        if lang == "de":   # German
            phrase = "Guten Morgen "
        elif lang == "fr": # French
            phrase = "Bonjour "
        elif lang == "it": # Italian
            phrase = "Buongiorno "
        elif lang == "tr": # Turkish
            phrase = "Günaydın "
        elif lang == "gr": # Greek
            phrase = "Καλημερα "
        else:
            phrase = "Hi "
        print("customized function is call")
        return phrase + name + "!"
    return customized_greeting

say_hi = greeting_func_gen("tr")
print(say_hi("Gülay")) 

def our_decorator(add):
    
    print("decorator call")
    def function_wrapper(x):
        print("Before calling function")
        add()
        print("after function call")
    return function_wrapper

def add(x,y):
    print("both value are added")

add=our_decorator(add)
add\

def my_decorator(func):
    def wrapper():
        var_1=10
        var_2=20
        print(f"value will added",{var_1+var_2})
        func()
        print(f"value will substract",{var_1-var_2})
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()

def our_decorator(func):
    print("decorator call")
    print(func)
    def wrapper():
        list=[1,2,3,4,5,6,7,8,9,10]
        even_count=0
        odd_count=0
        for i in list:
            if i%2==0:
                even_count+=1
            else:
                even_count+=1
        print(f"this is even count",even_count)
        func()
        print(f"this is odd count",odd_count)
    return wrapper

@our_decorator
def even_odd_func():
    print("even_odd_func call")
even_odd_func()

from random import random,randint,choice
def our_decorator(func):
    def function_1(*args,**kwargs):
    
        print("before function call")
        res=func(*args,**kwargs)
        print(res)
        print("after function call")
    return function_1

random=our_decorator(random)
random()

def decorator_1(func):
    print("decorator_1 function call")
    def decorator_code_1(*args,**kwargs):
        print("before decorator_1 function call")
        func()
        print("function call after return add")
        var_1=100
        var_2=200
        result=var_1+var_2
        print(f"first decorator function in add",result)
    return decorator_code_1

def decorator_2(func):
    print("decorator_2 function call")
    def decorator_code_2(*args,**kwargs):
        print("before decorator_2 function call")
        func()
        print("function call after retur substract")
        var_1=100
        var_2=200
        result=var_1-var_2
        print(f"second decorator function in substract",result)
    return decorator_code_2

@decorator_2        
@decorator_1
def my_function():
    print("two functions call")
print(my_function())

def my_decorator(arg1, arg2):
    print("decorator function call")
    def wrapper(func):
        print(func)
        def inner_wrapper():
        
            print("decorator argument",arg1,arg2)
            result=func()
            return result
        return inner_wrapper     
    return wrapper
    
@my_decorator(([1,2,3,4,5,6,7]),arg2={'name':"Rahul","age":24,"email":"Rahul@gmail.com"})
def function_1():
    return ""
print(function_1())

def evening_decorator(foo):
    print("evening decorator call")
    def function_wrapper(x):
        print("Good_evening"+function_wrapper.__name__+"")
        return foo(x)
    return function_wrapper

def morning_decorator(foo):
    print("morning decorator call")
    def function_wrapper_1(x):
        print("Good_morning"+function_wrapper_1.__name__+"")
        return foo(x)
    return function_wrapper_1
        
@evening_decorator 
@morning_decorator
def foo(x):
    print(42)
foo("hi")

def greeting(func_1):
    print("greeting decorator call")
    def function_wrapper(x,y):
        print(f'result will',x+y)
        print("hi, "+func_1.__name__+"")
        # print("hi, "+func_1.__doc__+"")
        print("hi, "+func_1.__module__+"")
    return function_wrapper

@greeting
def func_1(x,y):
    return x+y
func_1(10,20)

def decorator(func):
    print("decorator call func")
    def helper(x,y):
        print("decorating helper function,  "+func.__name__)
        func(x,y)
        print("decorating helper function after call,")
    return helper

@decorator
def func(x,y):
    print("inside func")
func(10,20)

class decorator_1:
    
    def __init__(self,func):
        self.func=func

    def __call__(self,*args,**kwargs):
        print("before decorator call")
        self.func(*args,**kwargs)
        print("after decorator call")
        
@decorator_1
def func_1(x,y):
    print("inside func",x+y)
func_1(10,20)

class Book():
  name="shri"
  age=25
  def __init__(self,writer,length):
    self.writer=writer
    self.length=length

  # def __str__(self):
  #   return f"{self.writer}"
  
  def disp(self):
    return self.writer
    #print(self.writer)
    
a=Book("Intro to Python","John Doe")
print(a)
d =print(a.disp())

class A:
    def __init__(self,*args):
        self.name=args

b=A([1,2,3,4,5],["Ankit"])
print(b.name[1][0])
print(b.name)

def func(x):
    print("hello")
x=(1,2,3)
func(x)

from typing import Any


class A:
    def __init__(self):
        print("class instance was initialized")

    def __call__(self,*args,**kwargs):
        print("Arguments are:",args,kwargs)
        print(args)
        print(kwargs)
x=A()
x(3,4,x=11,y=12)
print(x("hello","world",x=10,y=20))

def decorator_1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decorator(func):
    def inner():
        x=func()
        return 2*x
    return inner
@decorator_1
@decorator
def num():
    return 10
print(num())

import time
def timer(func):
    print("timer print is call")
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        start_time = time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Function took {end_time-start_time}")
        return result
    return wrapper
@timer      
def my_function():
    print("hello,world")
    time.sleep(5)
my_function()

import time
class my_decorator():
    print("decorator class call")
    def __init__(self):
        print("instance objects is call")

    def __call__(self,*args,**kwargs):
        self.start_time=time.time()
        result=self.my_function(*args,**kwargs)
        self.end_time=time.time()

@my_decorator
def my_function():
    time.sleep(5) 
    print("hello,world")
my_function()

import time as t
class my_decorator:
    print("decorator call")
    def __init__(self,delay_second):
        self.delay_second=delay_second

    def __call__(self,func):
      def wrapper(*args,**kwargs):
          t.sleep(self.delay_second)
          return func(*args,**kwargs)      
      return wrapper
                    
@my_decorator(5)
def my_function():
    print("hello,world")
my_function()

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))


def say_hello_decorator(func):
    def wrapper():
        print("before the function called")
        func()
        print("after the function called")
    return wrapper

@say_hello_decorator
def say_hello():
    print("this is function")
say_hello()

