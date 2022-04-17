import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Enter your choice of cards from A to K of diamonds or enter Q to quit:")
    if user_input.upper() == "Q":
        break
    else:
        random_card = random.choice(diamonds)
        hand.append(random_card)
        diamonds.remove(random_card)
    print("Your hand: ", hand)
    print("Remaining Cards: ", diamonds)

if not diamonds:
    print("There are no more cards to pick.")