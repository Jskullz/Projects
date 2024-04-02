import random
from gamedata import logo, data
import os
play_again = True
while play_again:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(logo)
    print("_________________________________________________________")
    already_seen=[]
    def get_random():
        choice=random.choice(data)
        while choice in already_seen:
            choice=random.choice(data)
        already_seen.append(choice)
        return choice

    print("Welcome to Higher or Lower")
    score=0
    choice2=get_random()
    playing = True
    while playing:
        choice1=choice2
        print(f"Your score is {score}")
        print("_________________________________________________________")
        print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
        choice2=get_random()
        print("vs")
        print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
        print("_________________________________________________________")

        user_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n\n")
        if user_choice=='A' and choice1['follower_count']>choice2['follower_count']:
            score+=1
            
        elif user_choice=='B' and choice2['follower_count']>choice1['follower_count']:
            score+=1
            
        else:
            print("_________________________________________________________")
            print(f"Sorry that's wrong. Final score: {score}")
            decide=input("Do you want to play again? Type 'yes' or 'no': ").lower()
            print("_________________________________________________________")
            print("\n")
            if decide=='no':
                play_again=False
                input("Press any key to exit")
                break
            else:
                play_again=True
                break









