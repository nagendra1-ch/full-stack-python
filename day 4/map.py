"""
import time
def fun(x):
    return x**3

start_time=time.perf_counter()
l=[3,5,2,4,5,6,3,2,9]
print(list(map(fun,l)))
end_time=time.perf_counter()
print(end_time-start_time)

"""
a=[]
for i in range(10):
    if i==0 or i==1:
        a.append(i)
    else:
        a.append(a[i-1]+a[i-2])
print(*a)