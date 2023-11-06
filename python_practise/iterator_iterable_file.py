# iterable objects in python
list=[1,2,3,4,4,6,7,7,8]
tuple=("hello","world","this","is","tuple")
set={100,200,300,400,122,132,3,1,313,3234243,312,12}
dict={"name":"rahul","age":24}
d=range(1,10)
print(d)

for item_iterable in list:
  print(item_iterable)

for tuple_iterable in tuple:
  print(tuple_iterable)

for set_iterable in set:
  print(set_iterable)

for key,value in dict.items():
  print(key,value)

class MyIterator:
    def __init__(self):
        self.counter=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter>=5:
            raise StopIteration
        else:
            self.counter+=1
            return self.counter

my_iterator=MyIterator()
print(my_iterator.__dict__)
for i in my_iterator:
    print(i)

list_1=[1,2,3]
iterator_obj=iter(list_1)
print(iterator_obj)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

cities = ["Paris", "Berlin", "Hamburg", 
          "Frankfurt", "London", "Vienna", 
          "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)

expertises = ["Python Beginner", 
              "Python Intermediate", 
              "Python Proficient", 
              "Python Advanced"]
expertises=iter(expertises)
print(next(expertises))
print(next(expertises))

other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

other_cities=iter(other_cities)
while other_cities:
    try:
        city=next(other_cities)
        print(city)
    except StopIteration:
        break

list_1=["indore","Bhopal","jabalpur","kareli","pune","mumbai"]
for i in list_1:
    print(type(i))

list_2=iter(list_1)
print(type(list_2))
print(next(list_2))
print(next(list_2))

def number_of_cities(start,end):
    for i in range(start,end+1):
        yield i
number=number_of_cities(1,5)
for n in number:
    print(n)

class cycle(object):
    def __init__(self,iterable):
        self.iterable=iterable
        self.iter_obj=iter(self.iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
               obj=next(self.iter_obj)
               return obj

            except StopIteration:
                self.iter_obj=iter(self.iterable)  
a=cycle("aabc")
print(a.__dict__)

for i in range(10):
    print(next(a),end=",")

def city_generator():
    yield "indore"
    yield "Bhopal"
    yield "pune"
    yield "mumbai"
  
gen=city_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def demo_generator():
    yield 1
    yield 2

gen=demo_generator()
print(next(gen))
print(next(gen))
print(next(gen))

class NumberIterator():
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        result=self.start
        self.start+=1
        print(result)

num_class=NumberIterator(10,1)
# print(num_class.__dict__) 
print(num_class)
   