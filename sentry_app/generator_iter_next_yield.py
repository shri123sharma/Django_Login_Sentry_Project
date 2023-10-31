ls1=[1,2,4,5,6,7,7,8]
print(ls1)
print(dir(ls1))
print(ls1.__dir__())

for i in ls1:
    print(i)
print(dir(i))

ls1=['first','second','third','fourth']
var1=iter(ls1)
print(dir(var1))
print(next(var1))


ts1=('first','second','third','fourth',10.23,23,4,5,6,8)
for i in ts1:
    print(i)


def func(b,a=None,c=None):
    return a+b+c
print(func(30,20,30))

# def method(a=None,b,c=None):
#     return a*b*c
# print(method(100,20,300))

def func1(*args):
    for i in args:
        return i
print(func1([10,20,30,40,5056,]))

def generator_function():
    for i in range(10):
        yield i
var=generator_function()
print(next(var))
print(next(var))

def fibonacci(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for x in fibonacci(10):
    print(x)


def fibo(n):
    a=b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result
print(fibo(10))


def generator(n):
    for i in range(n):
        yield i
gen=generator(10)
print(next(gen))
print(next(gen))

my_str="shrikant"
a=iter(my_str)
print(next(a))

int_var=1799
print(dir(int_var))
print(next(int_var))

