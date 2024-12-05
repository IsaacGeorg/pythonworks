
class Bank_account:
    def __init__(self,customer_name,mpin,account_type,balance):
        self.customer_name=customer_name
        self.__mpin=mpin                        # the __ before mpin activitates and accessed it as private inside class (protected)
        self.account_type=account_type
        self.__balance=balance
    def get_balance(self):
        print(self.__balance)                   # here balance is now accessed outside the class, thus it makes it public
bank_account_instance=Bank_account("Haridev",2834,"savings",2000)
# print(bank_account_instance.__mpin)
bank_account_instance.get_balance()