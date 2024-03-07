import random
import os
playing = True
def roll ():
    return random.randint(1,9)
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Fortune Teller!")
    print("______________________________")
    input("Press enter to start.")
    print("\n")

    print("Think of a question you would like to ask the fortune teller.")
    input("Press enter to continue.")
    print("\n")
    print("The fortune teller is thinking...")
    input("Press enter to reveal your fortune.\n\n")
    result=roll()
    if result == 1:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   It is certain.")
    elif result == 2:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   It is decidedly so.")
    elif result == 3:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Yes.")
    elif result == 4:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Reply hazy, try again.")
    elif result == 5:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Ask again later.")
    elif result == 6:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Concentrate and ask again.")
    elif result == 7:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   The answer is no.")
    elif result == 8:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Outlook not so good.")
    elif result == 9:
        print("THE FORTUNE TELLER SAYS:")
        print("---------------------------")
        print("   Very doubtful.")

    play_again = input("\n---------------------------\nWould you like to ask another question? (yes/no) ")
    while play_again.lower() != "yes" and play_again.lower() != "no":
        if play_again.lower()=="":
            break
        print("Invalid Input.")
        play_again = input("Would you like to ask another question? (yes/no) ")
    if play_again.lower() == "no":
        playing = False
        print("Goodbye.")
        input("Press enter to exit.")



    


