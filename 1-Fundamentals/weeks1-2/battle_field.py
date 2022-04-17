
"""game characters"""
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"


while True:
    """below variabes contain the hitpoints for each characters"""
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 90

    """ level of character damage """
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 110

    """ dragon hitpoint and damage"""

    dragon_hp = 300
    dragon_damage = 50

    while True:
        """show the character options to the player"""
        print("1) Wizard \n2) Elf \n3) Human")

        """ get player input"""
        character = input("Choose your character, enter 1 or wizard: ")

        if character == "1" or character.lower() == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "2" or character.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == "3" or character.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        else:
            print(
                "Unknown Character: Valid character inputs are 1 or wizrd, 2 or elf, 3 or human.")

    print("You have choosen the character: " + character + "\n" +
          "Health: " + str(my_hp) + "\n" + "Damage: " + str(my_damage))

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The " + character +
              " damaged the Dragon! \nThe Dragon's hitpoints are now: " + str(dragon_hp) + "\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break

        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at " + character + "\nThe " +
              character + "'s hitpoints are now: " + str(my_hp) + "\n")
        if my_hp <= 0:
            print(character + " has lost the battle")
            break

    game_continue = input(
        "Do you want to continue the game? Enter Y to continue or N to stop playing: ")
    if game_continue.lower() == "y":
        continue
    else:
        break
