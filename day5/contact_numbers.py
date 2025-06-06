from contact_functions1 import *
print("     --MENU--")
print("1.Add number\n2.Find Nunber\n3.Update Number\n4.Delete NUmber\n5.View all contacts\n6.exit")
try:
    
    while True:
        try:
            choice=int(input("enter your chioce:"))
            print()
            
            if choice==1:
                add_contacts()
                
            elif choice==2:
                retrive_number()
            elif choice==3:
                update_number()
            elif choice==4:
                delete_number()
            elif choice==6:
                print("exiting....")
                break
            elif choice==5:
                view_contacts()
            else:
                print("Enter valid choice")
                print()
        except Exception as e:
            print(e)
            print()
except Exception as e:
    print(e)

