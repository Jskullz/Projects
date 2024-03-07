import os
play_again = True
while play_again:
    playing = True
    bidders = {}
    highest_bid =0
    winner = ""
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    logo='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    print(logo)
    print("Welcome to the secret auction program.")
    while playing:
        name = input("Enter your name: ")
        valid_bid = False
        while not valid_bid:
            bid = input("Enter your bid: $")
            if bid.isdigit():
                bid = int(bid)
                valid_bid = True
            else:
                print("Invalid bid. Please enter a valid bid.")
        

        
        
        def add_bidder(name, bid,highest_bid, winner):
            bidders[name] = bid
            
            

        add_bidder(name, bid,highest_bid, winner)
        deciding_bidders = True
        while deciding_bidders:
            add_players = input("Are there any other bidders? Type 'yes' or 'no'.\n")
            if add_players == "yes":
                clear()
                deciding_bidders = False
                playing = True
            elif add_players == "no":
                clear()
                playing = False
                deciding_bidders = False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                
                True
    for name in bidders:
        if (bidders[name]) > highest_bid:
            highest_bid = bidders[name]
            winner = name

    print("""
__        _____ _   _ _   _ _____ ____  
\ \      / /_ _| \ | | \ | | ____|  _ \ 
 \ \ /\ / / | ||  \| |  \| |  _| | |_) |
  \ V  V /  | || |\  | |\  | |___|  _ < 
   \_/\_/  |___|_| \_|_| \_|_____|_| \_\ 
      """)
    print(f"{winner} wins with a bid of ${highest_bid}.")
    deciding_play = True
    while deciding_play:
        playing_again = input("Do you want to play again? Type 'yes' or 'no'.\n")
        if playing_again == "yes":
            clear()
            deciding_play = False
            play_again = True
        elif playing_again == "no":
            clear()
            print("Thank you for playing.")
            input("Press enter to exit.")
            deciding_play = False
            play_again = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            