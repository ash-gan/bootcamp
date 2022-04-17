import random
high_score = 0


def dice_game():
    global high_score
    print("Current High Score:" + str(high_score))
    while True:
        print("1) Roll Dice \n2) Leave Game")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            roll_1 = random.randint(1,6)
            roll_2 = random.randint(1,6)
            total_roll = roll_1 + roll_2 
            print("\nYou roll a... " + str(roll_1) + "\nYou roll a... " + str(roll_2) +  "\n\nYou have rolled a total of: " + str(total_roll) +"\n")
            if total_roll > high_score:
                high_score = total_roll
                print("New High Score!" + "\n\nCurrent High Score: "+ str(high_score))
        elif user_choice == "2":
            print("Goodbye!")
            break
dice_game()