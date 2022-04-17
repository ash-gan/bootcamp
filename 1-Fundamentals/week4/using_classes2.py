class User:

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password is changed to ", self.password)


class BankUser(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")
print(bankuser1.change_password("newworld"))
