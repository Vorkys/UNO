from random import randint
from time import sleep
"""
Add UNO option, if the player has 2 cards and can play he must write which card to use AND UNO (exp. 2 UNO)
If he does that he is out of trouble.
At the start of each player it prints the len of the others players.
"""
all_cards = ["0-R", "1-R", "1-R", "2-R", "2-R", "3-R", "3-R", "4-R", "4-R", "5-R", "5-R", "6-R", "6-R", "7-R", "7-R", "8-R", "8-R", "9-R", "9-R", "S-R", "S-R", "R-R", "R-R", "+2-R", "+2-R",
         "0-Y", "1-Y", "1-Y", "2-Y", "2-Y", "3-Y", "3-Y", "4-Y", "4-Y", "5-Y", "5-Y", "6-Y", "6-Y", "7-Y", "7-Y", "8-Y", "8-Y", "9-Y", "9-Y", "S-Y", "S-Y", "R-Y", "R-Y", "+2-Y", "+2-Y",
         "0-B", "1-B", "1-B", "2-B", "2-B", "3-B", "3-B", "4-B", "4-B", "5-B", "5-B", "6-B", "6-B", "7-B", "7-B", "8-B", "8-B", "9-B", "9-B", "S-B", "S-B", "R-B", "R-B", "+2-B", "+2-B",
         "0-G", "1-G", "1-G", "2-G", "2-G", "3-G", "3-G", "4-G", "4-G", "5-G", "5-G", "6-G", "6-G", "7-G", "7-G", "8-G", "8-G", "9-G", "9-G", "S-G", "S-G", "R-G", "R-G", "+2-G", "+2-G",
         "+4", "+4", "+4", "+4", "W", "W", "W", "W"]

def init():
    """vytvori hrace, rozda jim karty a ukaze nasledujici kartu"""
    global used_cards, cards, players, top_card, action, actual_player, num_players

    action = None                                                                                       #what the player does
    actual_player = 0                                                                                   #player to play

    cards = []                                                                                          #all the cards for the current game
    used_cards = []                                                                                     #all cards that are used by player and such in the game

    players = []                                                                                        #list of players and their cards(hands)

    for card in all_cards:                                                                              #creates the list "cards" so the game can be played many times without problems
        cards.append(card)

    while 2:
        num_players = int(input("Kolik bude hráčů? "))                                                  #asks how many players to add to "players"
        if num_players > 1 and num_players < 11:
            for n in range(1, num_players + 1):
                players.append([])
            break
        else:
            print("Tento počet nelze.")

    #print("Pocet hracu {} a celk karty {}". format(players, cards))

    for player in players:                                                                              #distribute the cards to the players
        for num_cards in range(7):
            _randcard = randint(0, len(cards) - 1)
            player.append(cards[_randcard])
            cards.pop(_randcard)

    #print(players)
    #print(cards)
    top_card = cards[randint(0, len(cards) - 1)]
    used_cards.insert(0, top_card)
    cards.remove(top_card)

    print("Karta na vrchu: {}".format(top_card))
    if len(top_card) < 3:

        while 1:
            rand_card = cards[randint(0, len(cards) - 1)]

            if len(rand_card) >= 3:
                number, color = rand_card.split("-")
                print("Barva karty: {}".format(color))
                break
    sleep(2)

def game():
    """Cast kde se hra hraje"""
    print(9000 * "\n")
    input("Hrac {} je pripraven?".format(actual_player + 1))
    print(" ".join(map(str, players[actual_player])))
    last_card()

    if action == 0:
        draw()

    
    next_player()

def draw():
    """hrac nemuze hrat takze lize"""
    rand_card = cards[randint(0, len(cards) - 1)]
    players[actual_player].append(rand_card)
    cards.remove(rand_card)

def last_card():
    """co je ted prave zahrano/na poli"""
    if len(used_cards) > num_players:
        print("Karty zahrané v posledním kole: {}".format(used_cards[0: len(players)] ))
    else:
        print("Karty zahrané v posledním kole: {}".format(* used_cards))

def draw_two():
    """lize nebo posila dal ale +2"""
    if top == 0:
        rand_card = cards[randint(0, len(cards) - 1)]
        players[actual_player].append(rand_card)
        cards.remove(rand_card)

def draw_four():
    """lize 4*"""
    #zavola se i wild
    pass

def wild():
    """hrac zmeni barvu nez zacne dalsi hrac"""
    pass

def next_player():
    """kolobeh order"""
    pass

def stop():
    """hrac vynecha nasledujiciho hrace"""
    pass

def Main_menu():
    """starting menu"""
    n = int(input("New game?(1 - yes, 0 - no) "))
    #start = n.upper()
    if n == 1:
        init()
        game()
        Main_menu()
    else:
        input("Game over.")

Main_menu()
