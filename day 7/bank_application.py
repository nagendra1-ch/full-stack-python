from abc import ABC,abstractmethod
print()
class BankAccount(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    def withdraw(self,money):
        pass
    def deposit(self):
        pass

class SavingsAccount(BankAccount):
    __balance=0
    def get_balance(self):
        return f"Balance in the account: {self.__balance}"
    def withdraw(self,money):
        self.__balance-=money
        print(f"remaining Balance: {self.__balance}")
    def deposit(self,money):
        self.__balance+=money
        print("updated successfully")

class CurrentAccount(BankAccount):
    __balance=0
    def __init__(self,name,money):
        self.name=name
        self.__balance=money
    def get_balance(self):
        print("balance in the account: ",self.__balance)
    def withdraw(self,money):
        self.__balance-=money
        print(f"remaining Balance: {self.__balance}")
    def deposit(self,money):
        self.__balance+=money
        print("updated successfully")

class Bank:
    owner='bank'
    account_number=0
    def __init__(self,name,account_number,account_type="Savings"):
        self.owner=name
        self.account_number=account_number
        if account_type=="Savings":
            self.account=SavingsAccount()
        if account_type=="Current":
            self.account=CurrentAccount()
        
class Manager:

    def get_customer_info(self,bank_accountant:Bank):
        print(f"Owner name: {bank_accountant.owner}")
        print(f"Account Number: {bank_accountant.account_number}")
        print(f"Account Type: {"Savings Account" if type(bank_accountant.account)==SavingsAccount else "Current Acoount"}")
        print(bank_accountant.account.get_balance())


ram=Bank("ram",100,"Savings")
ram.account.deposit(100)
ram.account.get_balance()
c=Manager()
c.get_customer_info(ram)