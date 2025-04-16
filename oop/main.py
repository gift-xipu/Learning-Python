from classes.bankAccount import BankAccount

def main():
    bk = BankAccount("GM Xipu", 21243543, 20000)
    task = input("Hi, what would you like to do today? 1. Check Balance, 2. Withdraw, 2. Deposit")
    if task == '1':
        balance = bk.checkBalance()
        print(balance)

    elif task == '2':
        amount = float(input("How much would you like to Withdraw"))
        bk.withdraw = amount

    elif task == '3':
        amount = float(input("How much would you like to Deposit"))
        balance = bk.deposit(amount)
        print(balance)

    else:
        print("Wrong input")

if __name__ == "__main__":
    main()
