# map(function,iterable_object)
ls1=[10,20,30,40]
ls2=[]
for i in range(len(ls1)):
    ls2.append(ls1[i]**2)
print(ls2)

ls1=[1,2,3,4,5,6]
ls2=list(map(lambda x:x**2,ls1))
print(dir(lambda x:x**1))
print(ls2)

def func(number):
    return number**2
number=[1000,2000,3000,4000]
h1=list(map(func,number))
print(h1)

def func(n):
    return n**3
number=[1,2,3,4,5,6]
ls1=list(map(func,number))
print(ls1)

def multiply(x):
    return x**x
number=[10,20,30,40,5]
ls1=list(map(multiply,number))
print(ls1)

# def add(x):
#     return x+x
# def substract(x):
#     return x**x
# number=[10,20,30]
# func=(add,substract)
# ls1=list(map(func,number))
# print(ls1)

ls1=[1,2,3,4,5]
ls2=list(filter(lambda x:x>2,ls1))
print(ls2)

ls3=[1,2,3]
ls4=list(map(lambda x:x>2,ls3))
print(ls4)

product=1
ls1=[1,2,3,4,5]
for i in ls1:
    product=product*i
print(product)

from functools import reduce
ls1=[1,2,3,4,5]
ls2=reduce(lambda x,y:x*y,ls1)
print(ls2)


def gen_func(n):
    for i in n:
        yield i
gen=gen_func([10,20,30,40])
print(next(gen))

def func(a:int,b:int):
    return a+b
result=func(10,20)
print(result)


some_list=['a','b','c','b','d','e','f','n','n']
duplicate=[]
for i in some_list:
    if some_list.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)

some_list1=['a','b','c','b','c','d','f','n']
duplicate1=set([i for i in some_list1 if some_list1.count(i)>1])
print(duplicate1)

valid=set(['yellow','red','green','black'])
valid1=set(['blue','red','green'])
print(valid.intersection(valid1))

print(type(valid))
