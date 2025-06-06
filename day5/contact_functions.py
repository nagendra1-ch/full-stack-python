import math as m
contacts={}
def open_file():
     file=open("contact_details.txt","r")
     file1=file.readlines()
     for item in file1:
          data=item.split()
          contacts[data[0]]=int(data[1])
     file.close()
          
def add_contacts():
        try:
            name=input("Enter Name: ")
            phone_number=int(input("enter Contact number: "))
            a=int(m.log10(phone_number))+1
            b=[]
            b.append(phone_number)
            b=set(b)
            if a==10:
                contacts[name]=phone_number
                file=open("contact_details.txt","a")
                file.write(name+" "+str(phone_number)+"\n")
                file.close()
                
            else:
                print("enter valid number")
            print()
        except Exception as e:
             print(e)
             print()
def retrive_number():
        name=input()
        if name in contacts:
            print(f"phone number of {name} is {contacts[name]}")
        else:
             print("Not found")
        print()
def update_number():
        try:
            name=input("enter name:")
            phone_number=int(input("Enter Number:"))
            a=int(m.log10(phone_number))+1
            if a==10:
                if name in contacts:
                    contacts[name]=phone_number
                    file=open("contact_details.txt","w")
                    file.write("")
                    file.close()
                    file=open("contact_details.txt","a")
                    for item in contacts:
                         file.write(name+" "+str(phone_number)+"\n")
                    file.close()
                if name not in contacts:
                    contacts[name]=phone_number
            else:
                print("enter valid number")
        except Exception as e:
             print(e)
def delete_number():
        name=input("enter name:")
        if name in contacts:
            del contacts[name]
            file=open("contact_details.txt","w")
            file.write("")
            file.close()
            file=open("contact_details.txt","a")
            for item in contacts:
                    file.write(item+" "+contacts[item]+'\n')
            file.close()
            print("Deleted Successfully")
        else:
             print("Not Found")
        print()
def view_contacts():
    for i in contacts:
            print(f"{i} : {contacts[i]}")
    print()
