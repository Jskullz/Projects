#Create a game that chooses a random number between 1 and 100
#The user can choose hard or easy mode easy mode gives the user 10 guesses hard mode gives the user 5 guesses
#The user then guesses the number
#If the user guesses the number they win
#If the user doesn't guess the number they lose a life.

import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lose_life(lives, random_number, numbers_guessed, guess):
    if guess not in numbers_guessed and guess != random_number:
        lives -= 1
        numbers_guessed.append(guess)
        print(f"You have {lives} lives left")
        print(f"You have guessed: {numbers_guessed}")
        print("__________________________________________________________")
    elif guess in numbers_guessed:
        print("You have already guessed that number")
        print(f"You have {lives} lives left")
    return lives, numbers_guessed

def easy_mode():
    lives =10
    random_number = random.randint(1, 100)
    numbers_guessed = []
    print("Welcome to Easy mode of the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {lives} lives to guess the number!\n")
    print("__________________________________________________________")

    while lives > 0:
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print(f"Congratulations you guessed the number {random_number}!")
            print("That was the correct number! You are a pro!")
            print("Why not try hard mode next time?")
            print("__________________________________________________________")
            break
        elif guess  < random_number:
            print("The number you guessed is too low")
    
        elif guess > random_number:
            print("The number you guessed is too high")
            
        lives, numbers_guessed = lose_life(lives, random_number, numbers_guessed, guess)
           
            
        

        if lives == 0:
            print(f"You have run out of lives, the number was {random_number}")
            input("\nPress enter to continue")
            break

def hard_mode():
    lives =5
    random_number = random.randint(1, 100)
    numbers_guessed = []
    print("Welcome to Hard mode of the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {lives} lives to guess the number!\n")
    print("__________________________________________________________")

    while lives > 0:
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print(f"Congratulations you guessed the number {random_number}!")
            print("That was the correct number! You are a pro!")
            print("__________________________________________________________")
            break
        elif guess  < random_number:
            print("The number you guessed is too low")
    
        elif guess > random_number:
            print("The number you guessed is too high")
            
        lives, numbers_guessed = lose_life(lives, random_number, numbers_guessed, guess)
           
            
        

        if lives == 0:
            print(f"You have run out of lives, the number was {random_number}")
            input("\nPress enter to continue")
            break
        
        

def main():
    logo ="""

 _____                          _____  _             _   _                    _                  _ 
|  __ \                        |_   _|| |           | \ | |                  | |                | |
| |  \/ _   _   ___  ___  ___    | |  | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ | |
| | __ | | | | / _ \/ __|/ __|   | |  | '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|| |
| |_\ \| |_| ||  __/\__ \\_ _ \   | |  | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   |_|
 \____/ \__,_| \___||___/|___/   \_/  |_| |_| \___| \_| \_/ \__,_||_| |_| |_||_.__/  \___||_|   (_)
                                                                                                   
"""
    print(logo)
    print("Welcome to the number guessing game")
    mode = input("Choose a mode (easy/hard): ")
    clear()
    if mode == "easy":
        easy_mode()
    elif mode == "hard":
        hard_mode()
    else:
        print("Invalid mode")
        main()
playing=True
while playing:
    clear()
    main()
    if input("Would you like to play again? (yes/no): ") == "no":
        playing = False
        print("\nGoodbye")
        input("\nPress enter to exit")
        break
