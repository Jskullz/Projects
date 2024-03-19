import os
import random
playing=True
while playing:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def player_cards():
        return random.choice(cards)

    def dealer_cards():
        return random.choice(cards)

    player_cards_list = [player_cards(), player_cards()]
    dealer_cards_list = [dealer_cards(), dealer_cards()]

    bust = False

    def calculate_score(cards_list):
        score = sum(cards_list)
        while score > 21 and 11 in cards_list:
            cards_list.remove(11)
            cards_list.append(1)
            score = sum(cards_list)
        return score

    players_score = calculate_score(player_cards_list)
    dealers_score = calculate_score(dealer_cards_list)

    for card in player_cards_list:
        if card == 11:
            if players_score > 21:
                players_score -= 10

    for card in dealer_cards_list:
        if card == 11:
            if dealers_score > 21:
                dealers_score -= 10

    print(f"Your cards: {player_cards_list}\ncurrent score: {players_score}\n")
    print(f"Computer's first card: {dealer_cards_list[0]}\n")
    print("__________________________________________________________")

    if players_score == 21:
        if dealers_score == 21:
            print("\nDraw")
            input("\nPress enter to exit")
        else:
            print("\nYou win")
            input("\nPress enter to exit")

    choosing = True
    while choosing:
        hit_or_stand = input("\nType 'y' to get another card, type 'n' to pass: ")
        if hit_or_stand == "y":
            new_card = player_cards()
            player_cards_list.append(new_card)
            players_score = calculate_score(player_cards_list)
            print("__________________________________________________________")
            print(f"\nYour cards: {player_cards_list}, current score: {players_score}")
            print("\n")
            print(f"Computer's first card: {dealer_cards_list[0]}")
            print("__________________________________________________________")
            if players_score > 21:
                print (f"\nYou busted, your final hand: {player_cards_list}, final score: {players_score}")
                choosing = False
                bust=True
        elif hit_or_stand == "n":
            print(f"Your final hand: {player_cards_list}, final score: {players_score}")
            choosing = False
        else:
            input("Invalid input, press enter to try again\n")

    while dealers_score < 17 and bust == False:
        print(f"The computer's hand is currently {dealer_cards_list}, final score: {dealers_score}")
        new_card = dealer_cards()
        dealer_cards_list.append(new_card)
        dealers_score = calculate_score(dealer_cards_list)

    print(f"\nThe computer's final hand: {dealer_cards_list}, final score: {dealers_score}")
    print("________________________________________________________")

    def win_condition():
        if dealers_score > 21:
            print("\nYou win")
        elif players_score > 21:
            print("\nYou lose")
        elif dealers_score > players_score:
            print("\nYou lose")
        elif dealers_score == players_score:
            print("\nDraw")
        elif players_score > dealers_score:
            print("\nYou win")

    win_condition()

    def play_again():
        play = input("\nDo you want to play again? Type 'y' or 'n': ")
        if play == "y":
            clear()
        elif play == "n":
            global playing
            playing = False
        else:
            input("Invalid input, press enter to try again")
    
    play_again()
