

class Bank:
    def __init__(self,acno,balance,ac_type,customername):
        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.customername=customername
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Your account, acct.no {self.acno} has been credited with {amount}. Avail Balance: {self.balance}")
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print(f"Your account, acct.no {self.acno} has been debited with {amount}. Avail Balance: {self.balance}")
    def get_balance(self):
        print("Your Available Balance: ",self.balance)


instance1=Bank(137818212,2371,"savings","Adhil")
instance1.deposit(25000)
instance1.withdraw(100)
instance1.get_balance()
