def test_arv_args(f_arg,*args):
    print("first argument of value",f_arg)
    for arg in args:
        print("args first value",arg)

test_arv_args("shrikant","sharma","arun","tihaiya")


def func(name,age):
    print(f"my name is {name} and my age{age}")
func("shrikant","sharma")

def func(*name):
    for val in name:
        print(val)
func("user1","user2","user3","user4") 


def greet_me(**kwargs):
    for key,val in kwargs.items():
        print(f"this is key is {key} and value is {val}")
greet_me(name="shrikant")


def test_args_kwargs(arg1,arg2,arg3):
    print("first value",arg1)
    print("second value",arg2)
    print("third value",arg3)
# value=("two",5,3)
# test_args_kwargs(*value)

value={"arg1":1,"arg2":3,'arg3':5}
test_args_kwargs(**value)


# Monkey patching example
class original_class:
    def method_to_patch(self):
        return "original behaivour"

def new_method(self):
    return "pathched behaivour"

def again_new_method(self):
    return "second run time behaivour change"


original_class.patched_method=new_method
original_class.patch_method=again_new_method

    
obj1=original_class()
obj2=original_class()
obj3=original_class()
print(obj1.method_to_patch())
print(obj2.patched_method())
print(obj3.patch_method())

