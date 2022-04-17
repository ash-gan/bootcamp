from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register, donate

database = {"admin": "password123"}
donations = {}
authorized_user = ""

while True: 
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: " + authorized_user)

    user_option = int(input("Enter your choice: "))
    
    if user_option == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username.lower(), password)
    elif user_option == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username]=password
    elif user_option == 3:
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_amt = donate(authorized_user)
            if authorized_user not in donations:
                donations[authorized_user] = [donation_amt]
            else:
                donations[authorized_user].append(donation_amt)
    elif user_option == 4:
        print(donations)
        show_donations(donations)
    elif user_option == 5:
        print("Leaving DonateMe, Good bye!")
        break

