import time
def fun(n):
    sum1=0
    sum2=0
    while True:
            k=1
            for i in range(1,k+1):
                sum1+=i
            for i in range(k,n+1):
                sum2+=i
            if sum1==sum2:
                return k
            k=k+1
            if n==k:
                return -1
s=time.perf_counter()
print(fun(8))
e=time.perf_counter()
print(e-s)