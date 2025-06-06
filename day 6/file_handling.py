f=open("names.txt","w")
for i in range(10):
    f.writelines(str(i))
f.close