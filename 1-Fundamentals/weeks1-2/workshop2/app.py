'''
It's my banking application where you can register in the app if no account, login and perform banking transactions such as checking account balance, depositing the money to your account
withdrawing money and logout if no further actions needed. 
'''
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    

print("          === Automated Teller Machine ===          ")
balance =0 

while True: 
    name = input ("Enter name to register:")
    if not len(name) >= 1 and len(name) <= 10:
        print("the maximum name length is 10 characters.")
    else:
        break
   
while True: 
    pin = input("Enter PIN:")
    if len(pin) == 4 and pin.isdigit():
        break
    else:
        print("PIN must contain 4 numbers")

print(name+" has been registered with starting balance of $" + str(balance))


while True:
    print("          === Automated Teller Machine ===          " + "\nLOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter PIN:")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        new_balance = account.deposit(balance)
        balance = new_balance
        account.show_balance(balance)
    elif option == "3":
        new_balance = account.withdraw(balance)
        balance = new_balance
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break







