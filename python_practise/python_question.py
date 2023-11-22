def areRotation(s1,s2):
   l1=len(s1)
   l2=len(s2)
   if l1!=l2:
       return False
   s1+=s1
   if s2 in s1:
       return True
   else:
       return False
str1="geeksforgeeks"
str2="forgeeksgeeks"
print(areRotation(str1,str2))


def left_rotate(string,num):
    print(string[:num]+string[num:])
left_rotate("hello",2)

def right_rotate(string,num):
    print(string[-num:]+string[:-num])
right_rotate("hello",2)

def immediatesmaller(arr,n):
    # import pdb;pdb.set_trace()
    l1=[]
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            l1.append(arr[i+1])
        else:
            l1.append(-1)
            
        if i == n-2:
            l1.append(-1)
    return l1
num=5
array=[4,2,1,5,3]
print(immediatesmaller(array,num))

def factorial(N):
    if N==0 or N==1:
        return 1
    else:
        return N*(factorial(N-1))       
N=5
print(factorial(N))

# N = 7
# Arr[] = {1, 2, 3, 4, 5, 6, 7}
# D = 2
# Output: 3 4 5 6 7 1 2
# Explanation: 
# Rotate by 1: [2, 3, 4, 5, 6, 7, 1]
# Rotate by 2: [3, 4, 5, 6, 7, 1, 2]

def leftarrayrotate(arr,n,d):
  return arr[d:]+arr[:d]   
N=4
arr=[1,3,4,2]
d=3
print(leftarrayrotate(arr,N,d))

# Input :
# N = 9
# Output:
# 2
# Explanation:
# 1 and 4 are the only Perfect Squares
# less than 9. So, the Output is 2
import math

def countSquares(n):
    count=0
    for i in range(1,n):
        num = math.sqrt(i)
        if check_perfect(int(num), i):
            count+=1
            
    return count  

def check_perfect(rt, num):
    if rt*rt == num:
        return True
    else:
        return False
       
N=int(input("enter a number"))
print(countSquares(N))

def perfectsquare(N):
    sqrt_num=math.sqrt(N)
    print(sqrt_num)
    return sqrt_num.is_integer()

if __name__=="__main__":
    N=int(input("enter a number:-"))
    if perfectsquare(N):
        print(True)
    else:
        print(False)
        
def sortArr(arr, n): 
        #code here
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
if __name__=="__main__":
    N=4
    arr=[4,9,3,1]
    print(sortArr(arr,N))
    
