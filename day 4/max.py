
l=[7,3,2,14,1,0,20]

max_ele=l[0]
for i in range(len(l)):
    if max_ele<l[i]:
        max_ele=l[i]
print(max_ele)
