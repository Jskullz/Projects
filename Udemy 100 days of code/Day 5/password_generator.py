import random

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input! Please enter a valid integer.")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = get_integer_input("How many letters would you like in your password?\n")
    nr_symbols = get_integer_input("How many symbols would you like?\n")
    nr_numbers = get_integer_input("How many numbers would you like?\n")

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password = random_letters + random_numbers + random_symbols
    random.shuffle(password)
    password = ''.join(password)
    print(f"Your password is: {password}")

playing = True
while playing:
    generate_password()
    play_again = input("Would you like to generate another password? (yes/no) ").lower()
    if play_again != "yes":
        break
input("Press enter to exit")