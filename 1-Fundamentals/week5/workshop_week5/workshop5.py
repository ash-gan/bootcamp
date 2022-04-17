import random


def guess_random_num(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is:", random_number)
    user_guessed_numbers = []
    while tries > 0:
        print("Numebr of tries left: ", tries)
        user_input = int(input("Guess a number between " +
                               str(start) + " and " + str(stop) + ": "))
        # Implement bonus task 3
        if user_input in user_guessed_numbers:
            print(
                "Error!!! You have already guessed this number. Please try a different number.")
            continue
        else:
            user_guessed_numbers.append(user_input)
        # Implement bonus task 1
        if user_input not in range(start, stop+1):
            print("Error!!!, please enter a number between ", start, " and ", stop)
            continue
        if user_input == random_number:
            print("You guessed the correct number!")
            return
        elif user_input < random_number:
            print("Guess higher!")
        else:
            print("Guess lower!")
        tries -= 1
    print("Oops!!!!, you ran out of number of tries.")
    print("You failed to guess the number: ", random_number)


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is:", random_number)
    for item in range(start, stop+1):
        print("Number of tries left:", tries)
        print("The program is guessing...", item)
        if item == random_number:
            print("The progrm has guessed the correct number!")
            return True
        tries -= 1
        if tries == 0:
            print("The program failed to guess the correct number")
            return False


def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print("Random number to find:", random_number)
    numbers = range(start, stop+1)
    low = 0
    high = len(numbers)-1
    mid = 0
    while low <= high:
        print("Number of tries left: ", tries)

        mid = (high+low)//2
        print("The program is guessing...", numbers[mid])
        if numbers[mid] == random_number:
            print("The program has guessed the correct number!")
            break
        elif numbers[mid] < random_number:
            print("Guessing lower!")
            low = mid+1
        else:
            print("Guessing higher")
            high = mid-1
        tries -= 1
        if tries == 0:
            print("The program failed to guess the correct number")
            break


""" Driver Test Code"""
# guess_random_num(5, 1, 100)
# guess_random_num_linear(5, 1, 100)
# guess_random_num_binary(3, 1, 100)


# Implement bonus task 2
def get_user_input():
    number_of_tries = int(
        input("Please enter the number of tries you would like to set: "))
    start_number = int(input("Please set/choose the start number: "))
    stop_number = int(input("Please set/choose the stop number: "))
    print(
        "Input which algorithm you would like to use to search the target number. Your available options are")
    print("1. You guess the number" +
          "\n2. Linear search by computer" + "\n3. Binary search by computer")
    user_search_pref = int(input("Enter your choice: "))

    if user_search_pref == 1:
        guess_random_num(number_of_tries, start_number, stop_number)
    elif user_search_pref == 2:
        guess_random_num_linear(number_of_tries, start_number, stop_number)
    elif user_search_pref == 3:
        guess_random_num_binary(number_of_tries, start_number, stop_number)


def check_betting_requirements(user_balance, bet_value):
    if bet_value > user_balance:
        print("Error!!! Your bet is greate than your balance! Choose right bet.")
        return
    if bet_value < 1 or bet_value > 10:
        print("Bet value has to be between 1 to 10, increaments of 1")
        return
    res = guess_random_num_linear(5, 1, 10)
    return res

# Implement bonus task 4


def gambling_game():
    user_balance = 10
    while user_balance > 0 and user_balance < 50:
        print("You have $", user_balance, " availble to bet!")
        user_bet = input(
            "Do you think computer will guess the correct number? Y/N: ")
        if user_bet.lower() == "y":
            bet_value = float(input("What's your bet: "))
            res = check_betting_requirements(
                user_balance, bet_value)
            if res:
                print("You are on a roll!!!")
                bet_value *= 2
                user_balance += bet_value
            elif res == False:
                print("Ooops who loose the bet!")
                user_balance -= bet_value
            else:
                continue
        elif user_bet.lower() == 'n':
            bet_value = float(input("What's your bet: "))
            res = check_betting_requirements(
                user_balance, bet_value)
            if res:
                print("Ooops who loose the bet!")
                user_balance -= bet_value
            elif res == False:
                print("You are on a roll!!!")
                bet_value *= 2
                user_balance += bet_value
            else:
                continue
        else:
            print("Enter a valid input Y or N")

    if user_balance <= 0:
        print("Your balance is ", user_balance, " you loose the game")
    elif user_balance > 50:
        print("Congratulations!!! you won $", user_balance)


get_user_input()
gambling_game()
