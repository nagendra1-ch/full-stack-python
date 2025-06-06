from abc import ABC,abstractmethod
class Container(ABC):
    @abstractmethod
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def get_balance(self):
        pass
class Bank(Container):
    def create_account(self):
        name=input("Enter Your name: ")
        account_number=int(input("Set your account number: "))
        balance=0
        file=open("bank_file.txt","a")
        file.write(name+" "+str(account_number)+" "+str(balance)+"\n")
        file.close()
    def deposit(self):
        try:
            file=open("bank_file.txt","r")
            account_number=input("Enter Account Number: ")
            account_details=file.readlines()
            file.close()
            data1=''
            flag=False
            for details in account_details:
                data=details.split()
                if data[1]==account_number:
                    money1=int(input("Enter amount you want to deposit: "))
                    money=int(data[2])
                    money+=money1
                    flag=True
                    data[2]=str(money)
                    print("Amount Deposited Successfully..")
                details=data[0]+" "+data[1]+" "+data[2]
                data1=data1+details+"\n"
            if not flag:
                print("Details Not Found")
            file=open("bank_file.txt","w")
            file.write(data1)
            file.close

        except Exception as e:
            print(e)
    def withdraw(self):
        try:
            file=open("bank_file.txt","r")
            account_number=input("Enter Account NUmber: ")
            account_details=file.readlines()
            file.close()
            data1=''
            flag=False
            for details in account_details:
                data=details.split()
                if data[1]==account_number:
                    money1=int(input("Enter amount you want to Withdraw: "))
                    money=int(data[2])
                    money-=money1
                    flag=True
                    data[2]=str(money)
                    print("Amount Debited Successfully..")
                details=data[0]+" "+data[1]+" "+data[2]
                data1=data1+details+"\n"
            if not flag:
                print("Details Not Found")
            file=open("bank_file.txt","w")
            file.write(data1)
            file.close

        except Exception as e:
            print(e)
        
    def get_balance(self):
        try:
            file=open("bank_file.txt","r")
            account_number=input("Enter Account Number: ")
            account_details=file.readlines()
            file.close()
            data1=''
            flag=False
            for details in account_details:
                data=details.split()
                if data[1]==account_number:
                    print(f"Owner:{data[0]}    Account Number:{data[1]}     Balance: {data[2]}")
                    flag=True
            if not flag:
                print("Details Not Found..\n")

        except Exception as e:
            print(e)
    def manager(self):
        try:
            pin=int(input())
            if pin==123:
                file=open("bank_file.txt","r")
                account_details=file.readlines()
                file.close()
                for details in account_details:
                    data=details.split()
                    print(f"Owner:{data[0]}    Account Number:{data[1]}     Balance: {data[2]}")
            else:
                print("invalid details")
                        
            

        except Exception as e:
            print(e)
try:
    print("\n------MENU------\n1.Create Account\n2.Deposit Money\n3.Withdraw Money\n4.Get Balance\n5.Manager\n6.Exit\n")
    obj=Bank()
    while True:
        choice=int(input("\nEnter Your Choice: "))
        print()
        if choice==1:
            obj.create_account()
        elif choice==2:
            obj.deposit()
        elif choice==3:
            obj.withdraw()
        elif choice==4:
            obj.get_balance()
        elif choice==5:
            obj.manager()
        elif choice==6:
            print("Thanks for Visiting.....!")
            break
        else:
            print("Enter Valid Choice\n")
except Exception as e:
    print(e)