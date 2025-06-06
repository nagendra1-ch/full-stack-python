student={
        "name":"nagendra","age":19,"marks":[91,96,87],"present":True
    }
print(student)
avg=sum(student["marks"])/len(student["marks"])
print(avg)
for i in student.values():
    print(i)