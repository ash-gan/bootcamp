
def login(database, username, password):
    if username in database and database[username] == password:
        print("Welcome back "+ username +"!")
        return username
    elif username in database and database[username] != password:
        print("Incorrect password for  "+ username +"."+ " Please enter correct password to login.")
        return ""
    else:
        print("User not found. Please register!")
        return ""

    

def register(database, username, password):
    if username.lower() in database:
        print("Username already registered.")
        return ""
    else:
        if len(username) > 10 and len(password) < 5:
            print("Username cannot be over 10 characters and the password must be at least 5 characters.")
            return ""
        else:
            print("Username "+ username + " has been registered.")
            return username

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    if donation_amt.isdigit() == False:
        print("Enter a valid numeric input for donations.")
    elif float(donation_amt) <= 0:
        print("Enter a valid numeric input for donations.")
    else:
        donation_string = username + " donated $" + str(donation_amt)
        print("Thank you! " + donation_string)
        return float(donation_amt)




