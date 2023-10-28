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


