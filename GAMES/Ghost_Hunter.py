import random
import os

playing = True

while playing == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    possessed = False
    escaped = False
    found_ghost = False
    dead = False

    # Display the introductory message only once with some spaces for readability
    
    print("""
▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒
▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒
▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒
▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒     
▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒       Welcome to the haunted hotel!
▒▒▒▌────────▌▒▒▒▒▒▒▒
▒▒█─────────▐▒▒▒▒▒▒▒  You are a ghost hunter hired by the owner to 
▒▐▌─▐───────▐▄▄▒▒▒▒▒
▒▐▌─▐────────▄▀▀█▒▒▒    find the ghost and escape the hotel.
▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒
▐▌────██▀█░█▄▒▄▄█▀▀▌     You are in the lobby of the hotel
▐▌──▌▐───▐░░▐▀░░░░░▌
▐▌──▌────▐░░▐░░░░░░▌
▐───▌────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█─────▀█▐▄▄▄█▀▀▒
▀▄▄─▐───────▄█▒▒▒▒▒▒
▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒
▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒\n""")
    
    
    


    def dice_roll():
        input("\nPress enter to roll the dice\n_____________________________\n")

        roll = random.randint(1, 6)
        print("You rolled a", roll)
        return roll

    def escape():
        global escaped, dead
        roll = dice_roll()
        if roll > 3:
            print("\nYou have escaped the hotel and you receive a reward of 100 dollars. You can now go home to your wife and kids and live happily ever after.")
            escaped = True
        else:
            print("\nYou have not escaped the hotel.")
            print("The ghost has killed you and now that you are dead, you and the ghost are now best friends and will go to the beach and haunt the hotel together.")
            dead = True

    def find_ghost():
        global found_ghost
        roll = dice_roll()
        if roll > 3:
            print("\nYou have found the ghost! Now you must escape the hotel and report your findings to the owner.")
            found_ghost = True
        else:
            print("\nYou have not found the ghost. Please keep looking.")
            found_ghost = False

    def possession():
        global possessed, dead
        roll = dice_roll()
        if roll < 3:
            print("\nYou have been possessed by the ghost!")
            possessed = True
            dead = True
        else:
            print("\nYou have not been possessed by the ghost. You are safe for now. Keep searching for the exit.")
            possessed = False
            dead = False


    while not escaped and not dead:
        choice = input("Would you like to [investigate] or [ask owner] for information on previous owners? ")
        if choice == "investigate":
            find_ghost()
            if found_ghost:
                resist_possession = input("\nYou feel a tingle down your spine and the ghost is trying to possess you. Would you like to [resist] or [give in]? ")
                if resist_possession.lower() == "resist":
                    possession()
                    if not dead:
                        escape_choice = input("\nWould you like to try to escape the hotel? (yes/no) ")
                        if escape_choice.lower() == "yes":
                            escape()
                        else:
                            print("\nYou have decided not to look for the exit and the ghost has killed you. You are now dead and you and the ghost are now best friends and will go to the beach and haunt the hotel together.")
                            dead = True
                else:
                    print("\nYou have given in to the ghost and you are now possessed.")
                    possessed = True
                    dead = True
        elif choice == "ask owner":
            print("\nThe owner tells you that the hotel was built on a cemetery and the ghost haunts the basement.")
            choice = input("Would you like to investigate the basement? (yes/no) ")
            if choice.lower() == "yes":
                find_ghost()
                if found_ghost:
                    resist_possession = input("\nYou feel a tingle down your spine and the ghost is trying to possess you. Would you like to [resist] or [give in]? ")
                    if resist_possession.lower() == "resist":
                        possession()
                        if not dead:
                            escape_choice = input("\nWould you like to try to escape the hotel? (yes/no) ")
                            if escape_choice.lower() == "yes":
                                escape()
                            else:
                                print("\nYou have decided not to look for the exit and the ghost has killed you. You are now dead and you and the ghost are now best friends and will go to the beach and haunt the hotel together.")
                                dead = True
                    else:
                        print("\nYou have given in to the ghost and you are now possessed.")
                        possessed = True
                        dead = True
                        
            else:
                print("\nYou have decided to leave the hotel and go home to your wife and kids, thinking that the hotel is too scary.")
                escaped = True
                dead = False
               

    if escaped:
        print("\nCongratulations! You have successfully escaped the haunted hotel. You win!")
        escaped = True
    play_again = input("\nWould you like to play again? (yes/no) ")
    if play_again.lower() == "no":
        playing = False
        input("Press enter to exit")
