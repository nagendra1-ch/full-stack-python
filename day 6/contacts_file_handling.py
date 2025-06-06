f=open("sample.txt","r")
num_dict={}
f=f.readlines()
for line in f:
    data=line.split()
    print(data)
    num_dict[data[0]]=int(data[1])
print(num_dict)
