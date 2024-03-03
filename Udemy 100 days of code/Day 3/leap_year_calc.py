playing = True

while playing == True:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Leap Year Checker!\n_________________________________")

    year = int(input("Type a year you would like to check for a leap year: "))
    print("\nChecking...\n")
    input("Press enter to see the result")

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is NOT a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")

    flip_again = input("\nWould you like to check another year? (yes/no)").lower()
    if flip_again == "no":
        playing = False
        input("Press enter to exit")
