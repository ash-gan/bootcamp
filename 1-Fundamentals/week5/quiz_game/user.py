import csv


class User:

    def __init__(self) -> None:
        self.database = {}
        with open("users.csv") as self.csv_file:
            self.csv_reader = csv.reader(self.csv_file)
            line_count = 0
            for row in self.csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.database[row[0]] = row[1]
                    line_count += 1

    def login(self, username, password):
        if username in self.database and self.database[username] == password:
            print("Welcome back " + username + "!")
            return username
        elif username in self.database and self.database[username] != password:
            print("Incorrect password for  " + username + "." +
                  " Please enter correct password to login.")
            return "invalid password"
        else:
            print("User not found. Please register!")
            return "user not found"

    def register(self, username, password):
        if username.lower() in self.database:
            print("Username already registered.")
            return ""
        else:
            if len(username) > 10 and len(password) < 5:
                print(
                    "Username cannot be over 10 characters and the password must be at least 5 characters.")
                return ""
            else:
                print("Username " + username + " has been registered.")
                data = [username, password]
                with open('users.csv', 'a', encoding='UTF8') as cs_file:
                    writer = csv.writer(cs_file)
                    writer.writerow(data)
                return username

    # Enhancements
    def update_user_game(self):
        pass
