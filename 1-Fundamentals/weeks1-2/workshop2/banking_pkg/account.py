def show_balance(balance):
    print("Current balance: $" + str(balance))

def deposit(balance):
    amount = float(input("Enter the amount to deposit:"))
    return (amount+balance)

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Where are you going to get that kind of money?")
        return balance
    else:
        new_balance = balance - amount
        return new_balance

def logout(name):
    print("Goodbye " +name+"!")
    

