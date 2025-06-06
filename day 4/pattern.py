def fun():
    n=5
    it=0
    while n>0:
        it+=1
        for j in range(it):
                if n==0:
                    return it-1
                n-=1
        
print(fun())