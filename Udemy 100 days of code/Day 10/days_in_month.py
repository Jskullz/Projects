import os
playing = True
while playing == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_month(year, month):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        leap = is_leap(year)
        if leap:
            month_days[1] = 29
        return month_days[month - 1]

    # Check for valid year and month inputs
    def get_valid_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid integer.")

    year = get_valid_input("What year would you like to check: ")
    month = get_valid_input("What month would you like to check: ")

    if month < 1 or month > 12:
        print("Invalid month. Please enter a month between 1 and 12.")
    else:
        days = days_in_month(year, month)
        print(f"The month of {month} in {year} has {days} days.")
    play_again = input("Do you want to check another month? (yes/no) ")
    while play_again.lower() != "yes" and play_again.lower() != "no":
        print("Invalid input.")
        play_again = input("Do you want to check another month? (yes/no) ")
    if play_again.lower() == "no":
        playing = False
        print("Goodbye.")
        input("Press enter to exit.")
        
