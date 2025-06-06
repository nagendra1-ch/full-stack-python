import time
"""
def fun(ele):
    l=[2,3,5,7,9,11,14]
    for i in l:
        if i==ele:
            return "element found"
    return "element not found"

start_time=time.perf_counter()

print(fun(14))
end_time=time.perf_counter()
print("end time=",end_time-start_time)"""
start_time=time.perf_counter()
x=14
list=[2,3,5,7,9,11,14]

for i in list:
    if i==x:
        print("found")
        break
else:
        print("not found")
end_time=time.perf_counter()
print(end_time-start_time)