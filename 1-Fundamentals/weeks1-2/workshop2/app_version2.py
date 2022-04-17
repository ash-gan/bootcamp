from banking_pkg import account

class app:

    def __init__(self):
        self.name = ""
        self.pin = 0
        self.balance = 0
        self.register_user()
        

    def atm_menu(self):
        print("")
        print("          === Automated Teller Machine ===          ")
        print("User: " + self.name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")

    def register_user(self):
        while True: 
            self.name = input ("Enter name to register:")
            if len(self.name) >= 1 and len(self.name) <= 10: 
                break        
            else:
                print("the maximum name length is 10 characters.")
                continue  

        while True:
            self.pin = input("Enter PIN:")
            if len(self.pin) == 4 and self.pin.isdigit():
                break
            else:
                print("PIN must contain 4 numbers")
                continue    
        print(self.name+" has been registered with starting balance of $" + str(self.balance))


    def login(self):
        while True:
            name_to_validate = input("Enter name:")
            pin_to_validate = input("Enter PIN:")
            if name_to_validate == self.name and pin_to_validate == self.pin:
                print("Login successful")
                break
            else:
                print("Invalid credentials!")


""" begining of the program execution"""
print("          === Automated Teller Machine ===          ")
#register a new user
my_app = app()
#request for input credentials to login
my_app.login()


while True:
    my_app.atm_menu()
    option = input("Choose an option:")
    if option == "1":
        account.show_balance(my_app.balance)
    elif option == "2":
        new_balance = account.deposit(my_app.balance)
        my_app.balance = new_balance
        account.show_balance(my_app.balance)
    elif option == "3":
        new_balance = account.withdraw(my_app.balance)
        my_app.balance = new_balance
        account.show_balance(my_app.balance)
    elif option == "4":
        account.logout(my_app.name)
        break