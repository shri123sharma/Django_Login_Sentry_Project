print("hello_world")
a=10
b=20
print(a+b)

def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()
obj1=formatted_name('shrikant','sharma')
print(obj1)

