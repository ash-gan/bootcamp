def show_homepage():
    filler = "-"
    print("        === DonateMe Homepage ===" + "\n" +
           42*filler + 
          "\n| 1.   Login      | 2.   Register        |" + "\n" + 42*filler + 
          "\n| 3.   Donate     | 4.   Show Donations  |" + "\n" + 42*filler + 
          "\n|              5.  Exit                  |" + "\n" + 42*filler)


def show_donations(donations):
    print("\n---All Donations---")
    total_donations = 0
    if donations:
        for username, donation_list in donations.items():
            for item in donation_list:
                print(username + " donated  $" + str(item))
                total_donations += item
    else:
        print("Currently there are no donations.")
    print("Total = $" + str(total_donations))




