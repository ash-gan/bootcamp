class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        if name == self.name:
            print("New name provided should be different than the existing name")
            return False

        if len(name) < 2 or len(name) > 10:
            print(
                "password characters length between 2-10 characters, please provide valid password.")
            return False
        else:
            self.name = name
            return True

    def change_pin(self, pin):
        if pin == self.pin:
            print("New PIN provided should be different than the existing PIN")
            return False
        if len(str(pin)) != 4 or str(pin).isdigit() != True:
            print("pin should be 4 digits, please provide valid pin.")
            return False
        else:
            self.pin = pin

    def change_password(self, password):
        if password == self.password:
            print("New password provided should be different than the existing password")
            return
        if " " in password:
            print(
                "password shouldn't contain any spaces, please provide password with no spaces.")
            return
        if len(password) < 5:
            print(
                "password characters length should be 5 or more, please provide different password.")
            return
        else:
            self.password = password


""" Driver Code for Task1

user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)

Driver Code for Task1 is complete"""


"""Driver Code for Task2"""
user2 = User("Ryan", 5678, "ironman")
print(user2.name, user2.pin, user2.password)

# valid inputs test for changing name, pin and password
user2.change_name("Jackson")
user2.change_pin(2222)
user2.change_password("betterment")
print(user2.name, user2.pin, user2.password)
"""End - - > Driver Code for Task2 is complete"""


""" Driver code for testing Bonus Task 3"""
user2 = User("Ryan", 5678, "ironman")
# Test user name length <=2 and <=10
user2.change_name("Alwaysthinkingoflonnames")
# Test password less than 5 length
user2.change_password("hulk")
# Test pin errors
user2.change_pin(558979)
user2.change_pin("her")

"""End - - > Driver Code for Bonus Task 3"""


class BankUser(User):

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def update_hold(self):
        if self.on_hold == False:
            self.on_hold = True
        else:
            self.on_hold = False

    def show_balance(self):
        print(self.name + " has an account balance of " +
              "{:.2f}".format(self.balance))

    def check_balance(self, amount):
        """ check if balance is less than requested amounnt """
        if amount > self.balance:
            print(
                "Not enough funds!!!. Transaction amount has to be for <= ", self.balance)
            return False
        return True

    def check_amount(self, amount):
        """ This method checks is amount value is valid positive number"""
        if amount < 0 or str(amount).isdigit() != True:
            print(
                "Invalid amount, please enter positive integer as amount to withdraw")
            return False
        return True

    def check_if_hold(self):
        """Checks instance's on_hold status and returns True of on_hold is True else False"""
        if self.on_hold == True:
            print(
                "This account is on hold, please contact your bank at 1-800-try-bank for more info.")
            return True
        return False

    def withdraw(self, amount):
        if self.check_if_hold():
            return

        if not self.check_amount(amount):
            return

        if not self.check_balance(amount):
            return

        self.balance -= float(amount)

    def deposit(self, amount):
        if self.check_if_hold():
            return

        if not self.check_amount(amount):
            return

        self.balance += amount

    def transfer_money(self, to_user, amount):
        if self.check_if_hold():
            return

        if to_user.check_if_hold():
            return

        if not self.check_amount(amount):
            return

        if not self.check_balance(amount):
            return

        print("Authetication required")
        transfering_user_pin = input(
            "Please provide your PIN to athorize money transfer: ")

        if self.pin == int(transfering_user_pin):
            if self.balance < amount:
                print("Insufficient funds for the transfer quest of $" +
                      str(amount) + " Transaction calncelled.")
                return False

            print("Transfer Authorized" + "\nYou are transferring $" +
                  str(amount) + " to " + to_user.name)
            to_user.balance += amount
            self.balance -= amount
            return True
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

    def request_money(self, from_user, amount):
        if self.check_if_hold():
            return

        if from_user.check_if_hold():
            return

        if not self.check_amount(amount):
            return

        if not self.check_balance(amount):
            return

        print("You are requesting " + str(amount) + "from " +
              from_user.name + "\nUser Authetication is required")
        user_pin = input("Enter " + from_user.name + "'s PIN: ")
        if from_user.pin == int(user_pin):
            user_password = input("Enter your password: ")
            if self.password == user_password:
                if from_user.balance < amount:
                    print("Insufficient funds for the transfer quest of $" +
                          str(amount) + " Transaction calncelled.")
                    return False
                self.balance += amount
                from_user.balance -= amount
                return True
            else:
                print("Invalid password. Transaction cancelled")
                return False
        else:
            print("Invalid PIN. Transaction cancelled")
            return False


"""Driver Code for Task3"""
bankuser1 = BankUser("Carol", 4444, "captainmarvel")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
"""End - - > Driver Code for Task3 is complete"""


"""  Driver Code for Task4"""
bankuser2 = BankUser("Steve", 3456, "captainamerica")
bankuser2.show_balance()
bankuser2.deposit(1000)
bankuser2.show_balance()
bankuser2.withdraw(200)
bankuser2.show_balance()
"""End - - > Driver Code for Task4 complete """


""" Driver Code for Task5"""
# user instance
bankuser3 = BankUser("Thor", 6666, "godofthunder")
bankuser4 = BankUser("Loki", 7777, "godofmischief")
bankuser4.deposit(5000)
bankuser4.show_balance()
transfer_result = bankuser4.transfer_money(bankuser3, amount=500)
bankuser4.show_balance()
bankuser3.show_balance()

if transfer_result:
    bankuser4.request_money(bankuser3, amount=500)
bankuser4.show_balance()
bankuser3.show_balance()
"""End - - > Driver Code for Task5 complete """


""" Driver Code for Bonus Task 1, 2, 5 """
bankuser2 = BankUser("Steve", 3456, "captainamerica")
bankuser2.deposit(1200)
bankuser2.withdraw(200)
bankuser2.show_balance()
# Test Bonus Task 2 implemetation, check amount requested greater than the balance
bankuser2.withdraw(2200)
bankuser2.show_balance()
# Test Bonus Task 5 by putting account on_hold True and try to withdraw, then put it back to on_hold status False
bankuser2.update_hold()
bankuser2.withdraw(200)
bankuser2.update_hold()
# ------- check transfer and request money Bonus task logic
bankuser2 = BankUser("Steve", 3456, "captainamerica")
bankuser2.deposit(1200)
# Test Bonus Task 2 for transfering money when amount is greater than balance
bankuser3 = BankUser("Bruce", 9807, "strongestavenger")
bankuser2.transfer_money(bankuser3, 2400)
# Test Bonus Task 5 for putting bankuser2 on_hold True and try to transfer the money
bankuser2.update_hold()
bankuser2.transfer_money(bankuser3, 200)
bankuser2.update_hold()
# Test Bonus Task 5 for putting bankuser2 on_hold True and trying to request the money
bankuser2.transfer_money(bankuser3, 200)
bankuser2.update_hold()
bankuser2.request_money(bankuser3, 200)
bankuser2.update_hold()
"""End - - > Driver Code for Bonus Task 1, 2, 5 """
