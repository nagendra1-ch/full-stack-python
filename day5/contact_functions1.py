def add_contacts():
    try:
        name=input("Enter name:")
        phone_number=int(input("enter phone number: "))
        file=open("contacts1.txt","a")
        file.write(name+" "+str(phone_number)+'\n')
        file.close()
    except Exception as e:
        print(e)
def retrive_number():
    try:
        name=input("enter name: ")
        file=open("contacts1.txt","r")
        data=file.readlines()
        flag=False
        for item in data:
            split_data=item.split()
            if name in split_data[0]:
                print(f"{split_data[0]}: {int(split_data[1])}\n")
                flag=True
        file.close()
        if not flag:
            print("Data Not Found")

    except Exception as e:
        print(e)
def update_number():
    try:
        name=input("enter name: ")
        file=open("contacts1.txt","r")
        data=file.readlines()
        data1=""
        file.close()
        for item in data:
            split_data=item.split()
            if name==split_data[0]:
                phone_number=input("enter phone number: ")
                split_data[1]=phone_number
            item=split_data[0]+" "+split_data[1]
            data1=data1+item+"\n"
        file=open("contacts1.txt","w")
        file.write(data1)
        file.close()
        
    except Exception as e:
        print(e)
def delete_number():
        name=input("enter name: ")
        file=open("contacts1.txt","r")
        data=file.readlines()
        data1=""
        file.close()
        for item in data:
            split_data=item.split()
            if name==split_data[0]:
                continue
            else:
                item=split_data[0]+" "+split_data[1]
                data1=data1+item+"\n"
        file=open("contacts1.txt","w")
        file.write(data1)
        file.close()
def view_contacts():
    try:
        file=open("contacts1.txt","r")
        data=file.readlines()
        flag=False
        for item in data:
            split_data=item.split()
            print(f"{split_data[0]}: {int(split_data[1])}\n")
        file.close()

    except Exception as e:
        print(e)