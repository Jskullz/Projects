import os

playing = True
guessed_numbers = []

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

def reset_streak():
    guessed_numbers.clear()

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("               Welcome to FizzBuzz!")
    print("             ________________________")
    print("""       
                  How to play:
            -------------------------
                Guess a number!
  Your goal is to guess 3 fizzbuzz numbers in a row!
        Can you figure out the pattern?
         """)
    input("Press enter to start.")
    os.system('cls' if os.name == 'nt' else 'clear')
    numbers_guessed_correctly = 0

    while numbers_guessed_correctly < 3:
        number = input("Guess the next number: ")
        while not number.isdigit():
            print("Invalid input. please enter a number.\n")
            number = input("Guess the next number: ")
        number = int(number)

        if number in guessed_numbers:
            print(f"You have already guessed {number} as a FizzBuzz number!")
            input("Press enter to continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if fizzbuzz(number) == "FizzBuzz":
            print(f"{number} is a FizzBuzz number!")
            guessed_numbers.append(number)
            numbers_guessed_correctly += 1
            print(f"You have guessed {numbers_guessed_correctly} FizzBuzz numbers correctly!")
            input("Press enter to continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif fizzbuzz(number) == "Fizz" or fizzbuzz(number) == "Buzz":
            print(f"{number} is a {fizzbuzz(number)} number!")
            reset_streak()
            numbers_guessed_correctly = 0
            print("Your current streak 0.")
            input("Press enter to continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"{number} is NOT a Fizz, Buzz, or FizzBuzz number.")
            reset_streak()
            numbers_guessed_correctly = 0
            print("Your current streak 0.")
            input("Press enter to continue.")
            os.system('cls' if os.name == 'nt' else 'clear')

    print("Congratulations! You have guessed 3 FizzBuzz numbers in a row!")
    keep_playing = input("Do you want to play again? (yes/no) ").lower()
    while keep_playing != "yes" and keep_playing != "no":
        print("Invalid Input.")
        keep_playing = input("Do you want to play again? (yes/no) ").lower()
    if keep_playing == "no":
        playing = False
        print("Goodbye.")
        input("Press enter to exit.")
