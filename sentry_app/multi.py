from multiprocessing import Process
import time
start_time=time.perf_counter()
def worker_function(number):
    result= number*number
    print(f"worker{number}*{number}={result}")

ls1=[1,2,3,4,5,6,7,8]
for i in ls1:
    worker_function(i)
end_time=time.perf_counter()
total_time=end_time-start_time
print(f"this is total execuation time {total_time}")


start_time=time.perf_counter()
def worker_function1(number1):
    print(f"Cube is {number1*number1*number1}")

def worker_function2(number2):
    print(f"Square is{number2**number2}")

if __name__=="__main__":
    p1=Process(target=worker_function1,args=[5])
    p2=Process(target=worker_function2,args=[10])

    p1.start()
    p2.start()

end_time=time.perf_counter()
total_time=end_time-start_time
print(f"total time in execuation{total_time}")

import threading
import time

start_time = time.perf_counter()

def func(second):
    print(f"this task run by{second}")
    return time.sleep(second)

# func(5)
# func(2)
# func(1)

t1=threading.Thread(target=func,args=[5])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)




