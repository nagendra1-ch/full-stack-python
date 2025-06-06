def add_student():
    name=input("Enter student Name: ").lower()
    marks=list(map(int,input("Enter marks: ").split()))
    grade_book[name]=marks
    print()
def view_marks():
    for i in grade_book:
        print(f"{i}:{grade_book[i]} avg_marks={round(sum(grade_book[i])/len(grade_book[i]),2)} ")
        print()
def search():
    name=input("Enter Student Name: ").lower()
    for i in grade_book:
        if name in i:
            print(f"{i}:{grade_book[i]} avg_marks={round(sum(grade_book[i])/len(grade_book[i]),2)} ")
            print()
def update():
    name=input("Enter student name: ").lower()
    marks=list(map(int,input().split()))
    if name in grade_book:
        grade_book[name]=marks
        print("updated successfully")
    else:
        print("Data Not Found")
    print()

def delete_student():
    name=input().lower()
    if name in grade_book:
        del grade_book[name]
        print("Deleted Successfully")
        print()
    else:
        print("Details not found")


grade_book={}
print("---Grades Book---")
print("1.Add Student\n2.View Students Data\n3.Search\n4.Update\n5.Remove Student\n6.Exit")
print()
while True:
    choice=int(input("enter your choice:"))
    print()
    if choice==1:
        add_student()
    elif choice==2:
        view_marks()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        delete_student()
    elif choice==6:
        print("Exiting....")
        break