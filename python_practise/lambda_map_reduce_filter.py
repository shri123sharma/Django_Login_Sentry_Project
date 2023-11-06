def func_1(x,y):
    return x+y
print(func_1(3,4))

sum=lambda x,y:x+y
print(sum(3,4))

numbers=[1,2,3,4,4,66,7,7]
def func_2(x):
    return x*2
squared_number=map(func_2,numbers)
squared_to_list=list(squared_number)
print(squared_to_list)

numbers=[1,2,3,4,5,6,7,8,9,10]
def func_1(x):
    if x%2==0:
      return True
    else:
        return False
even_num=list(map(func_1,numbers))
print(even_num)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_num=list(map(lambda x:x%2==0,numbers))
odd_num=list(map(lambda x:x%2!=0,numbers))
print(even_num)
print(odd_num)

numbers=[1,2,3,4,4,5,6,7,7,8,8,9,9,10]
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers)

even_num=list(map(lambda x:x%2==0,numbers)).__class__
print(even_num)

numbers=[1,2,3,4,5,6,7,7,8,9,10]
even_num=list(filter(lambda x:x%2==0,numbers))
odd_num=list(filter(lambda x:x%2!=0,numbers))
print(even_num)
print(odd_num)

# from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers)

numbers=[1,2,3,4,5,6,7,8,9,10]
squared_numbers=list(filter(lambda x:x**2,numbers))
print(squared_numbers)

numbers=[1,2,3,4,5,6,7,8,9,10]
reduce_nummber=reduce(lambda x,y:x//y,numbers)
print(reduce_nummber)

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers=list(filter(lambda x:x%2!=0,fibonacci))
even_numbers=list(filter(lambda x:x%2==0,fibonacci))
print(even_numbers)
print(odd_numbers)

# Reduce function in use to lambda function if and sequence collection is available to perform the all value calculate in python reduce function.

import functools
a=functools.reduce(lambda x,y:x+y,[10,11,12])
print(a)

b=functools.reduce(lambda x,y:x+y,range(1,10))
print(b)

c=functools.reduce(lambda x,y:x*y,range(1,10))
print(c)

# Every iterable object in iterator function but every iterator function not iterable of the python.

list_1=[1,2,3,4,5,6,7,8,9,9,10]
tuple_1=(10,20,30,40,50)
set_1={1,2,3,4,5,6,8,89}
dict_1={"name":"shri","value":{'list':[1,2,3,4,6,67]}}
# a1=10
print(type(iter(list_1)))
print(type(iter(tuple_1)))
print(type(iter(set_1)))
print(type(iter(dict_1)))
# print(type(iter(a1)))
p=iter(list_1)
print(next(p))

str="GeeksforGeeks"
rev_upper=lambda str:str.upper()[::-1]
print(rev_upper.__name__)

def cube(y):
    return y*y*y
print(cube(5))

y=5
l1=lambda y:y*y*y
print(l1)

add=lambda x,y:x-y if x>0 and y>0 else 0
print(add(2,3))
print(add(-2,3))