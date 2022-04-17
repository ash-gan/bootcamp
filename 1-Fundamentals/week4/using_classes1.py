""" class Player:
    max_hp = 4000


player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)
Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp) """


class Player:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Harry", 14000)
player2 = Player("Jackson", 15000)
print("P1:", player1.name, "----- HP", player1.hp, "-----score", player1.score)
print("P2:", player2.name, "----- HP", player2.hp, "-----score", player2.score)
