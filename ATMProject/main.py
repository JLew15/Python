import Bank
import Input

balance = Bank.ATM.getBalance()
print(str.format("Starting balance: {:.2f}", balance))
amount = Input.Validator.getFloat(Input.Validator,"Please enter a deposit amount ($0.00 - $1000.00", 0.00, 1000.00)
balance = Bank.ATM.deposit(amount)
print(str.format("New balance: {:.2f}", balance))
amount = Input.Validator.getFloat(Input.Validator,"Please enter a withdrawal amount ($0.00 - $1000.00", 0.00, 1000.00)
balance = Bank.ATM.withdraw(amount)
print(str.format("New balance: {:.2f}", balance))
