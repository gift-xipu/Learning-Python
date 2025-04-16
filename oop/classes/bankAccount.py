class BankAccount:
    def __init__(self, account_holder, account_num, balance):
        self.account_holder = account_holder
        self.__account_num = account_num
        self.__balance = balance

    @property
    def withdraw(self):
        pass

    @withdraw.setter
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Your balance is {self.__balance}")

    @property
    def deposit(self):
        pass

    @deposit.setter
    def deposit(self, amount):
        remaining_balance = self.__balance + amount
        return remaining_balance

    @property
    def checkBalance(self):
        return self.__balance
