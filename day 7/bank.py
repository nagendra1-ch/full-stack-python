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
class CurrentAcoount(BankAccount):
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

sa=SavingsAccount("nani",5000)
print("--------Savings Account----------\n")
sa.deposit(1000)
sa.get_balance()
sa.withdraw(2000)
sa.get_balance()
print()
ca=CurrentAcoount("nani",5000)
print("-------Current Account----------\n")
ca.deposit(1000)
ca.get_balance()
ca.withdraw(2000)
ca.get_balance()
print()