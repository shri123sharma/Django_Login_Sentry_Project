import threading

def count_n(n):
    count=0
    for _ in range(n):
        count+=1
    return count

def run_tasks():
    n=1000000
    num_threads=4
    threads=[]
    
    for i in range(num_threads):
        thread=threading.Thread(target=count_n,args=(n,))
        threads.append(thread)
        
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
import time 
start_time=time.time()
run_tasks()
end_time=time.time()
print(f"total time in run task {end_time-start_time}")

