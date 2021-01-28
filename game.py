import random

cards = ["0-R", "1-R", "1-R", "2-R", "2-R", "3-R", "3-R", "4-R", "4-R", "5-R", "5-R", "6-R", "6-R", "7-R", "7-R", "8-R", "8-R", "9-R", "9-R", "S-R", "S-R", "R-R", "R-R", "+2-R", "+2-R",
         "0-Y", "1-Y", "1-Y", "2-Y", "2-Y", "3-Y", "3-Y", "4-Y", "4-Y", "5-Y", "5-Y", "6-Y", "6-Y", "7-Y", "7-Y", "8-Y", "8-Y", "9-Y", "9-Y", "S-Y", "S-Y", "R-Y", "R-Y", "+2-Y", "+2-Y",
         "0-B", "1-B", "1-B", "2-B", "2-B", "3-B", "3-B", "4-B", "4-B", "5-B", "5-B", "6-B", "6-B", "7-B", "7-B", "8-B", "8-B", "9-B", "9-B", "S-B", "S-B", "R-B", "R-B", "+2-B", "+2-B",
         "0-G", "1-G", "1-G", "2-G", "2-G", "3-G", "3-G", "4-G", "4-G", "5-G", "5-G", "6-G", "6-G", "7-G", "7-G", "8-G", "8-G", "9-G", "9-G", "S-G", "S-G", "R-G", "R-G", "+2-G", "+2-G",
         "+4", "+4", "+4", "+4", "W", "W", "W", "W"]

_cards = []

used_cards = []

player_one = []
player_two = []
player_three = []
player_four = []

last_card = ""

def init():
    """Give all the 7 cards to each player"""
    global player_one, player_two, player_three, player_four, _cards, cards, used_cards

    player_one = []
    player_two = []
    player_three = []
    player_four = []
    _cards = []

    for prvek in cards:
        _cards.append(prvek)
###########################################################
    #if len(_cards) == 108:
    #    print("Balik je plny")
    #else:
    #    print("balik neni plny")
###########################################################

    for card in range(7):
        _random = random.randint(0, len(_cards) - 1)
        player_one.append(_cards[_random])

        used_cards.append(_cards[_random])

        del _cards[_random]

    for card in range(7):
        _random = random.randint(0, len(_cards) - 1)
        player_two.append(_cards[_random])

        used_cards.append(_cards[_random])

        del _cards[_random]

    for card in range(7):
        _random = random.randint(0, len(_cards) - 1)
        player_three.append(_cards[_random])

        used_cards.append(_cards[_random])

        del _cards[_random]

    for card in range(7):
        _random = random.randint(0, len(_cards) - 1)
        player_four.append(_cards[_random])

        used_cards.append(_cards[_random])

        del _cards[_random]
###########################################################

def begin():
    """Reveal the first card so the game can begin"""

    global _cards, used_cards, last_card

    _pass = False
    _random = random.randint(0, len(_cards) - 1)
    while _pass == False:
        if _cards[_random] == "W" or _cards[_random] == "+4":
            _random = random.randint(0, len(_cards) - 1)
        else:
            _pass = True

    last_card = _cards[_random]

    used_cards.append(_cards[_random])

    del _cards[_random]

def player_move():
    """Player are putting cards here"""
    global player_one, player_two, player_three, player_four, last_card

    reverse = False
    to_play = 0
    turns = [1, 2, 3, 4]

    while 1:
        if to_play >= 4:
            to_play = to_play % 4

        if turns[to_play] == 1:
            #print(9000 * "\n")
            print("Hraje hrát jedna!! Ostatni nekoukejte se!!!")
            input("Continue...")
            print("Karta na poli: {}".format(last_card))
            print("Tvoje karty jsou: {}".format(" ".join(map(str, player_one))))

            move = int(input("Select card: "))
            last_card = player_one[move - 1]

            used_cards.append(player_one[move - 1])
            del player_one[move - 1]


            if reverse == False:
                to_play += 1
            else:
                to_play -= 1

        elif turns[to_play] == 2:
            #print(9000 * "\n")
            print("Hraje hrát dva!! Ostatni nekoukejte se!!!")
            input("Continue...")
            print("Karta na poli: {}".format(last_card))
            print("Tvoje karty jsou: {}".format(" ".join(map(str, player_two))))

            move = int(input("Select card: "))
            last_card = player_two[move - 1]

            used_cards.append(player_two[move - 1])
            del player_two[move - 1]


            if reverse == False:
                to_play += 1
            else:
                to_play -= 1

        elif turns[to_play] == 3:
            #print(9000 * "\n")
            print("Hraje hrát tri!! Ostatni nekoukejte se!!!")
            input("Continue...")
            print("Karta na poli: {}".format(last_card))
            print("Tvoje karty jsou: {}".format(" ".join(map(str, player_three))))

            move = int(input("Select card: "))
            last_card = player_three[move - 1]

            used_cards.append(player_three[move - 1])
            del player_three[move - 1]


            if reverse == False:
                to_play += 1
            else:
                to_play -= 1

        elif turns[to_play] == 4:
            #print(9000 * "\n")
            print("Hraje hrát ctyri!! Ostatni nekoukejte se!!!")
            input("Continue...")
            print("Karta na poli: {}".format(last_card))
            print("Tvoje karty jsou: {}".format(" ".join(map(str, player_four))))

            move = int(input("Select card: "))
            last_card = player_four[move - 1]

            used_cards.append(player_four[move - 1])
            del player_four[move - 1]


            if reverse == False:
                to_play += 1
            else:
                to_play -= 1
        

def play_game():
    """main menu for the player"""

    n = input("New game(1/ano/yes): ")
    start = n.upper()
    if start == "1" or start == "ANO" or start == "YES":                                                        #asks if the player wish to play a new game
        init()
        begin()
        player_move()

        play_game()
    else:                                                                                                       #ends the program
        print("Game over.")
        input()

play_game()
