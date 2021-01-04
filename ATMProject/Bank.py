class ATM:
    balance = 20.00
    def deposit(amount):
        print(str.format("Depositing {:.2f}",amount))
        ATM.balance += amount
        return ATM.balance

    def withdraw(amount):
        if ATM.balance >= amount:
            print(str.format("Withdrawing {:.2f}", amount))
            ATM.balance -= amount
        else:
            print("Insufficient Funds")
        return ATM.balance
    def getBalance():
        return ATM.balance