def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before the function call")
        result=func(*args,**kwargs)
        print("after the function call")

    return wrapper


def my_add_decorator(func):
    def wrapper(*args,**kwrgs):
        print("before func called")
        result=func(*args,**kwrgs)
        return result*2
        print("after func called")
    return wrapper

def my_cap_decorator(func):
    # import pdb;pdb.set_trace()
    def change_func(*args,**kwargs):
        print("before func called")
        result=func(*args,**kwargs)
        return result
    return change_func